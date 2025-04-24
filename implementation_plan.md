# Implementatieplan: Hybride Scraper Configuratie

**Doel:** Implementeren van een nieuw configuratiesysteem voor website scrapers. Dit systeem scheidt de declaratieve configuratie (wat te scrapen en waar het te vinden is) in een JSON-structuur (opgeslagen in de database) van de uitvoerende logica en scraper runtime configuratie (hoe te scrapen, inclusief `crawl4ai` instellingen), die in Python klassen wordt gedefinieerd. Het bestaande, tabel-gebaseerde configuratiesysteem blijft behouden als fallback-mechanisme.

**Kernprincipes:**

1.  **Hybride Model:** JSON (DB) definieert de data-structuur (selectors, URLs, velden); Python code definieert de procesflow en runtime gedrag.
2.  **Flexibiliteit:** Site-specifieke Python klassen kunnen de basisimplementatie overerven en aanpassen voor complexe websites of specifieke `crawl4ai` configuraties per stap.
3.  **Onderhoudbaarheid:** JSON blijft gefocust en relatief eenvoudig. Complexe, site-specifieke logica wordt beheerd in versie-gecontroleerde Python code.
4.  **Backward Compatibility:** Het systeem valt terug op de oude configuratiemethode (bestaande tabellen en scraper-logica) als er geen nieuwe JSON-configuratie beschikbaar is voor een website.
5.  **Geen Runtime Config in DB:** Instellingen specifiek voor de scraper-engine (zoals `crawl4ai`'s `CrawlerRunConfig`, timeouts, browseropties, wachtstrategieën) worden **niet** in de JSON opgeslagen, maar beheerd binnen de Python code.

---

## Fase 1: Voorbereiding en Basisstructuur

1.  **Database Schema Aanpassing:**
    *   **Actie:** Creëer een nieuwe tabel in de database, genaamd `website_scrape_configs`.
    *   **Velden:**
        *   `id` (INT, Primary Key, Auto-increment)
        *   `website_identifier` (VARCHAR, Uniek, Not Null): Een unieke string die de website identificeert (bv. "vesteda", "pararius_v2", "nieuwe_site"). Deze identifier wordt gebruikt om de configuratie te koppelen aan de juiste Python scraper klasse.
        *   `config_json` (JSON of TEXT, Not Null): Bevat de volledige JSON-configuratie string voor de website. Kies het datatype dat het beste past bij de gebruikte database (JSON biedt vaak validatie en query-mogelijkheden).
        *   `version` (INTEGER, Nullable, Default 1): Optioneel veld voor versiebeheer van de configuratie.
        *   `is_enabled` (BOOLEAN, Not Null, Default TRUE): Vlag om deze JSON-configuratie snel te activeren/deactiveren.
        *   `created_at` (TIMESTAMP, Not Null, Default CURRENT_TIMESTAMP)
        *   `updated_at` (TIMESTAMP, Not Null, Default CURRENT_TIMESTAMP on update)
    *   **Belangrijk:** De bestaande tabellen die gebruikt worden voor het oude configuratiesysteem moeten **onaangetast blijven**.

2.  **Pydantic Modellen Definiëren:**
    *   **Locatie:** Bij voorkeur in een specifieke module, bv. `models/config_models.py`.
    *   **Actie:** Definieer een set Pydantic modellen die de structuur van de `config_json` valideren en parsen.
    *   **Hoofdmodel:** `WebsiteConfig`.
    *   **Submodellen:** `MultiStepConfig`, `SitemapConfig`, `LoginConfig`, `NavigationConfig`, `FilteringConfig`, `FilterStep`, `ExtractionConfig`, `ExtractionField`, `TransformationRule`, etc. (baseer de exacte structuur op de eerder besproken JSON-voorbeelden).
    *   **Cruciaal:** Zorg ervoor dat **geen** van deze modellen een veld bevat voor algemene of per-stap `scraper_options` (zoals browser type, timeouts, etc.). Deze horen thuis in de Python code.

3.  **Configuratie Laadmechanisme:**
    *   **Locatie:** Bij voorkeur in een repository/service module, bv. `services/repositories/json_config_repository.py`.
    *   **Actie:** Implementeer een klasse, bv. `JsonConfigRepository`.
    *   **Kernfunctionaliteit:** Definieer een asynchrone methode:
        ```python
        async def get_config_by_identifier(self, identifier: str) -> Optional[WebsiteConfig]:
            # 1. Query de 'website_scrape_configs' tabel voor de record met de gegeven 'website_identifier' en 'is_enabled = TRUE'.
            # 2. Als geen record gevonden wordt, retourneer None.
            # 3. Haal de 'config_json' string op.
            # 4. Probeer de JSON string te parsen en te valideren met Pydantic's WebsiteConfig.parse_raw().
            # 5. Bij succes, retourneer het gevalideerde WebsiteConfig object.
            # 6. Bij een JSONDecodeError of ValidationError: log de fout uitgebreid (inclusief identifier) en retourneer None.
        ```
    *   **Afhankelijkheden:** Deze repository heeft waarschijnlijk een database connectie/sessie nodig.

---

## Fase 2: Implementatie van Scraper Klassen

4.  **BaseWebsiteScraper Klasse:**
    *   **Locatie:** `crawlers/base_scraper.py`.
    *   **Actie:** Creëer een abstracte of basisklasse `BaseWebsiteScraper`.
    *   **Constructor:**
        ```python
        def __init__(self, crawler: AsyncWebCrawler, config: WebsiteConfig):
            self.crawler = crawler # crawl4ai (of andere) crawler instantie
            self.config = config   # Het gevalideerde Pydantic config object
            self.standard_run_config = self._build_standard_run_config()
        ```
    *   **Standaard `CrawlerRunConfig`:** Implementeer een private methode `_build_standard_run_config() -> CrawlerRunConfig`.
        *   Deze methode definieert de *default* runtime configuratie voor `crawl4ai`.
        *   Haal basisinstellingen (bv. browser path, headless mode) eventueel uit environment variables of een globale applicatieconfiguratie, maar **niet** uit `self.config`.
        *   Retourneer een `CrawlerRunConfig` object (of equivalent voor de gebruikte library).
    *   **Implementeer Standaard Scrape Methoden:** Implementeer asynchrone methoden voor de kernstappen van het scrape proces (maak ze eventueel `@abstractmethod` als de basisklasse abstract is, of bied een generieke implementatie):
        *   `async def login_async(self) -> bool:` (Gebruikt `self.config.strategy_config.login_config` en `self.standard_run_config`).
        *   `async def navigate_to_gallery_async(self) -> None:` (Gebruikt `self.config.strategy_config.navigation_config` en `self.standard_run_config`).
        *   `async def apply_filters_async(self) -> None:` (Gebruikt `self.config.strategy_config.filtering_config` en `self.standard_run_config`).
        *   `async def extract_gallery_async(self) -> AsyncGenerator[Dict[str, Any], None]:` (Gebruikt `self.config.strategy_config.gallery_extraction_config` en `self.standard_run_config`).
        *   `async def extract_details_async(self, url: str) -> Dict[str, Any]:` (Gebruikt `self.config.strategy_config.detail_page_extraction_config` en `self.standard_run_config`).
        *   `async def run_async(self) -> List[Dict[str, Any]]:` (Orchestreert de aanroep van de bovenstaande methoden in de juiste volgorde).
        *   Deze methoden lezen selectors, URLs, en extractie-instructies uit `self.config`, maar gebruiken `self.standard_run_config` (of een kopie daarvan) voor de interacties via `self.crawler`.

5.  **Site-Specifieke Scraper Klassen:**
    *   **Locatie:** Bij voorkeur in een aparte submap, bv. `crawlers/site_specific/`. Maak een bestand per site, bv. `crawlers/site_specific/nieuwe_site_scraper.py`.
    *   **Actie:** Voor websites die afwijken van de standaard flow of specifieke `crawl4ai` instellingen per stap vereisen, creëer een klasse die erft van `BaseWebsiteScraper`.
        ```python
        from ..base_scraper import BaseWebsiteScraper
        # Andere imports...

        class NieuweSiteScraper(BaseWebsiteScraper):
            # ... (zie template hieronder voor details) ...
        ```
    *   **Override Methoden:** Override alleen de methoden uit `BaseWebsiteScraper` die aangepaste logica vereisen.
    *   **Aangepaste `CrawlerRunConfig`:** Definieer binnen de site-specifieke klasse (bv. in `__init__` of direct in de methode) specifieke `CrawlerRunConfig` objecten voor bepaalde stappen. Gebruik `self.standard_run_config.model_copy(update={...})` om voort te bouwen op de standaardconfiguratie.
    *   **Gebruik Aangepaste Config:** Roep `self.crawler` methoden aan met de specifieke `CrawlerRunConfig` binnen de overridden methoden (bv. `await self.crawler.aeval(..., config=self.specific_filter_config)`).

---

## Fase 3: Integratie en Fallback

6.  **Scraper Factory Aanpassen:**
    *   **Locatie:** Waar de huidige scraper factory zich bevindt (bv. `factories/scraper_factory.py`).
    *   **Actie:** Pas de factory aan om zowel het nieuwe JSON-systeem als het oude systeem te ondersteunen.
    *   **Mapping:** Definieer een mechanisme om `website_identifier` te koppelen aan site-specifieke klassen (bv. een dictionary):
        ```python
        from crawlers.base_scraper import BaseWebsiteScraper
        from crawlers.site_specific.nieuwe_site_scraper import NieuweSiteScraper
        # ... import andere specifieke scrapers ...

        SCRAPER_CLASSES = {
            "nieuwe_site": NieuweSiteScraper,
            # "vesteda": VestedaScraper, # Voorbeeld
            # Voeg hier andere site-specifieke scrapers toe
        }
        ```
    *   **Logica van de Factory Methode (bv. `get_scraper`):**
        ```python
        async def get_scraper(identifier: str, crawler: AsyncWebCrawler, config_repo: JsonConfigRepository, old_config_repo: OldConfigRepository) -> BaseWebsiteScraper: # Of een gezamenlijke interface

            # 1. Probeer nieuwe JSON config te laden
            website_config: Optional[WebsiteConfig] = await config_repo.get_config_by_identifier(identifier)

            if website_config:
                # Nieuwe config gevonden
                SpecificScraperClass = SCRAPER_CLASSES.get(identifier, BaseWebsiteScraper) # Fallback naar Base als geen specifieke klasse is gemapt
                print(f"Using scraper class {SpecificScraperClass.__name__} for identifier '{identifier}' with JSON config.")
                return SpecificScraperClass(crawler=crawler, config=website_config)
            else:
                # 2. Fallback naar oude configuratie systeem
                print(f"JSON config not found or disabled for '{identifier}'. Attempting fallback to old configuration system.")
                old_config = await old_config_repo.get_config(identifier) # Gebruik de bestaande methode om oude config te laden

                if old_config:
                    # Oude config gevonden, instantieer de *oude* scraper klasse
                    from crawlers.old_system import OldScraperClass # Importeer de relevante oude scraper klasse
                    print(f"Using OLD scraper class OldScraperClass for identifier '{identifier}' with old config system.")
                    # Zorg dat de oude klasse compatibel is of maak een adapter
                    return OldScraperClass(crawler=crawler, old_config=old_config) # Pas aan naar constructor van oude klasse
                else:
                    # 3. Beide systemen falen
                    error_msg = f"No valid configuration found for website identifier '{identifier}' in either new JSON system or old system."
                    print(error_msg)
                    raise ValueError(error_msg) # Of een specifiekere exception
        ```
    *   **Afhankelijkheden:** De factory heeft de `JsonConfigRepository` en de repository/service voor het *oude* configuratiesysteem nodig.

7.  **Orchestratie:**
    *   **Actie:** Controleer de hoofdservice of -loop die het scraping proces start.
    *   **Aanpassing:** Zorg ervoor dat deze service de bijgewerkte `ScraperFactory` gebruikt om scraper instanties te verkrijgen. De manier waarop `scraper.run_async()` wordt aangeroepen en de resultaten worden verwerkt, hoeft waarschijnlijk niet te veranderen, aangezien de interface (idealiter) hetzelfde blijft.

---

## Startpunt: Template voor een Nieuwe Site-Specifieke Scraper

Dit template kan gebruikt worden als basis voor het implementeren van een scraper voor een nieuwe website (`nieuwe_site`) volgens het hybride model.

**1. JSON Configuratie (`nieuwe_site_config.json` - Voorbeeld):**

```json
{
  "website_identifier": "nieuwe_site", // Moet matchen met factory mapping & DB
  "website_name": "Mijn Nieuwe Voorbeeld Site",
  "base_url": "https://www.example-nieuwe-site.com",
  "is_active": true,
  "scrape_strategy": "multi_step", // Of "sitemap"
  "strategy_config": {
    // --- Login (Optioneel) ---
    "login_config": {
      "login_page_url": "/account/login",
      "username_selector": "input[name='username']",
      "password_selector": "input[name='password']",
      "submit_button_selector": "button#login-button",
      "post_login_check_selector": "a[href='/account/dashboard']" // Selector die aangeeft dat login succesvol was
    },
    // --- Navigatie naar overzicht ---
    "navigation_config": {
      "listings_page_url": "/properties/for-rent" // URL van de pagina met alle listings
    },
    // --- Filteren (Optioneel) ---
    "filtering_config": {
      "steps": [
        {
          "step_name": "Klik 'Huur'", "action": "click", "selector": "#property-type-filter button[data-value='rent']"
        },
        {
          "step_name": "Zet max prijs", "action": "input", "selector": "input#max-price", "value": "2000"
        },
        {
          "step_name": "Wacht op resultaten", "action": "wait", "wait_condition": {"type": "selector", "selector": ".listing-results.loaded"} // Expliciete wachtstap
        }
      ]
    },
    // --- Galerij Extractie ---
    "gallery_extraction_config": {
      "listing_item_selector": "article.property-card", // Selector voor elk item in de lijst
      "next_page_selector": "a.pagination-next:not(.disabled)", // Selector voor de 'volgende pagina' knop
      "max_pages": 5, // Optioneel: maximaal aantal pagina's om te scrapen
      "fields": [ // Velden om te extraheren van elk item in de lijst
        {"target_field": "url", "selector": "a.property-link", "extraction_type": "attribute", "attribute_name": "href", "is_required": true},
        {"target_field": "title", "selector": "h3.property-title", "extraction_type": "text", "is_required": true},
        {"target_field": "price_text", "selector": ".price-tag", "extraction_type": "text"}
      ]
    },
    // --- Detail Pagina Extractie ---
    "detail_page_extraction_config": {
      "fields": [ // Velden om te extraheren van de detailpagina
        {"target_field": "description", "selector": "#property-description > div", "extraction_type": "html"}, // Pak inner HTML
        {"target_field": "sqm", "selector": "li[data-label='Oppervlakte'] .value", "extraction_type": "text", "transformation_rule": [{"type": "parse_int"}]},
        {"target_field": "rooms", "selector": "li[data-label='Kamers'] .value", "extraction_type": "text", "transformation_rule": [{"type": "parse_int"}]}
      ]
    }
  }
}
```
*   **Opslaan:** Voeg deze JSON toe aan de `website_scrape_configs` tabel met `website_identifier = "nieuwe_site"`.

**2. Python Klasse (`crawlers/site_specific/nieuwe_site_scraper.py`):**

```python
import asyncio # Voor eventuele expliciete waits
from typing import Dict, Any, AsyncGenerator, Optional
import os # Voor environment variables (secrets)

from crawl4ai import AsyncWebCrawler
from crawl4ai.config import CrawlerRunConfig # Pas aan naar daadwerkelijke import

from models.config_models import WebsiteConfig # Jouw Pydantic modellen
from ..base_scraper import BaseWebsiteScraper

# Zorg dat deze klasse geregistreerd wordt in de SCRAPER_CLASSES dict in de factory
class NieuweSiteScraper(BaseWebsiteScraper):

    def __init__(self, crawler: AsyncWebCrawler, config: WebsiteConfig):
        """Initialiseert de scraper voor NieuweSite."""
        super().__init__(crawler, config)
        # Definieer hier site-specifieke run configs indien nodig
        self.login_run_config = self._build_standard_run_config().model_copy(update={
             "default_timeout_ms": 60000, # Meer tijd voor login interacties
             "wait_for_navigation": "domcontentloaded", # Wachtconditie na submit
        })
        self.detail_page_config = self._build_standard_run_config().model_copy(update={
             "block_resources": {"types": ["image", "stylesheet", "font"]} # Sneller laden van detailpagina
        })

    def _build_standard_run_config(self) -> CrawlerRunConfig:
        """Bouwt de standaard run config voor deze site."""
        # Haal eventueel basisinstellingen uit env vars
        headless_mode = os.getenv("SCRAPER_HEADLESS", "true").lower() == "true"
        return CrawlerRunConfig(
            browser="chromium", # Of "firefox", "webkit"
            headless=headless_mode,
            default_timeout_ms=30000,
            user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/...", # Goede user agent
            # Voeg andere standaard crawl4ai opties toe
        )

    async def login_async(self) -> bool:
        """Override login voor NieuweSite."""
        if not self.config.strategy_config.login_config:
            return True # Geen login nodig volgens config

        login_cfg = self.config.strategy_config.login_config
        # Construct full URL safely
        base = self.config.base_url.rstrip('/')
        login_path = login_cfg.login_page_url.lstrip('/')
        login_url = f"{base}/{login_path}"

        print(f"[{self.config.website_identifier}] Attempting login...")
        try:
            # Gebruik de specifieke login config
            await self.crawler.arun(url=login_url, config=self.login_run_config)

            # Haal credentials veilig op (NOOIT hardcoden!)
            username = os.getenv("NIEUWESITE_USERNAME")
            password = os.getenv("NIEUWESITE_PASSWORD")
            if not username or not password:
                print(f"[{self.config.website_identifier}] ERROR: Credentials not found in environment variables.")
                return False

            # Vul formulier in
            await self.crawler.aeval(f"document.querySelector('{login_cfg.username_selector}').value = '{username}'", config=self.login_run_config)
            await self.crawler.aeval(f"document.querySelector('{login_cfg.password_selector}').value = '{password}'", config=self.login_run_config)

            # Klik submit (wachtconditie is onderdeel van login_run_config)
            await self.crawler.aeval(f"document.querySelector('{login_cfg.submit_button_selector}').click()", config=self.login_run_config)

            # Optionele extra check na navigatie
            if login_cfg.post_login_check_selector:
                await self.crawler.aeval(f"document.querySelector('{login_cfg.post_login_check_selector}')", config=self.login_run_config.model_copy(update={"wait_for_selector": login_cfg.post_login_check_selector}))

            print(f"[{self.config.website_identifier}] Login successful.")
            return True
        except Exception as e:
            print(f"[{self.config.website_identifier}] Login failed: {e}")
            # Voeg hier specifiekere error logging toe (bv. screenshot maken)
            # await self.crawler.ascreenshot(path="login_error.png")
            return False

    async def apply_filters_async(self) -> None:
        """Override filter logica indien nodig."""
        # Voorbeeld: Als de basis implementatie volstaat, kun je deze methode weglaten
        # of expliciet de parent aanroepen:
        # print(f"[{self.config.website_identifier}] Applying filters using BaseWebsiteScraper logic...")
        # await super().apply_filters_async()

        # Als je specifieke logica nodig hebt:
        if not self.config.strategy_config.filtering_config:
             return
        filter_cfg = self.config.strategy_config.filtering_config
        print(f"[{self.config.website_identifier}] Applying custom filter logic...")
        step_config = self._build_standard_run_config() # Start met standaard config

        for step in filter_cfg.steps:
             print(f"  - Executing filter step: {step.step_name}")
             # Pas config aan voor deze specifieke stap indien nodig
             current_config = step_config

             if step.action == "click":
                 await self.crawler.aeval(f"document.querySelector('{step.selector}').click()", config=current_config)
             elif step.action == "input":
                 await self.crawler.aeval(f"document.querySelector('{step.selector}').value = '{step.value}'", config=current_config)
             elif step.action == "wait":
                 if step.wait_condition:
                     if step.wait_condition.type == "selector":
                         await self.crawler.aeval(f"document.querySelector('{step.wait_condition.selector}')", config=current_config.model_copy(update={"wait_for_selector": step.wait_condition.selector}))
                     elif step.wait_condition.type == "timeout":
                         await asyncio.sleep(step.wait_condition.duration_ms / 1000)
                     # Voeg andere wachttypes toe
             else:
                 print(f"    WARN: Unknown filter action '{step.action}'")

        print(f"[{self.config.website_identifier}] Custom filter logic applied.")


    async def extract_details_async(self, url: str) -> Dict[str, Any]:
        """Override detail extractie om specifieke config te gebruiken."""
        print(f"[{self.config.website_identifier}] Extracting details from {url} using specific config...")
        # Gebruik de specifieke detail_page_config
        # De daadwerkelijke extractie logica kan de implementatie van de base class gebruiken,
        # maar dan aangeroepen met de aangepaste config.
        # Of je kopieert/past de extractie logica hier aan.
        # Voorbeeld: Roep een (hypothetische) helper aan uit de base class met de custom config:
        # return await self._extract_fields_with_config(
        #     fields_config=self.config.strategy_config.detail_page_extraction_config.fields,
        #     target_url=url,
        #     run_config=self.detail_page_config
        # )
        # OF implementeer de extractie hier direct:
        extracted_data = {}
        try:
            await self.crawler.arun(url=url, config=self.detail_page_config)
            for field_cfg in self.config.strategy_config.detail_page_extraction_config.fields:
                 try:
                     # Implementeer extractie logica hier gebaseerd op field_cfg
                     # value = await self.crawler.aeval(...)
                     value = f"extracted_{field_cfg.target_field}" # Placeholder
                     # Pas transformaties toe
                     extracted_data[field_cfg.target_field] = value
                 except Exception as field_error:
                     print(f"  - Error extracting field '{field_cfg.target_field}': {field_error}")
                     if field_cfg.is_required: raise # Stop als vereist veld mist
            return extracted_data
        except Exception as page_error:
            print(f"[{self.config.website_identifier}] Failed to extract details from {url}: {page_error}")
            return {} # Retourneer leeg dict bij fout

    # --- Andere methoden ---
    # Override `navigate_to_gallery_async`, `extract_gallery_async`, `run_async`
    # alleen als de standaard implementatie van BaseWebsiteScraper niet volstaat.
```

**Conclusie:** Dit plan voorziet in de creatie van de nodige database structuur, Pydantic modellen, data access laag, basis scraper logica, en een factory die zowel het nieuwe als het oude systeem ondersteunt. Het bevat ook een gedetailleerd template dat als startpunt dient voor het implementeren van scrapers voor nieuwe websites volgens dit hybride model.
