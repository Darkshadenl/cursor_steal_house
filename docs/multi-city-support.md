# Multi-City Support voor StealHouse Scrapers

## Overzicht

De StealHouse scrapers ondersteunen nu configureerbare steden in plaats van hardcoded "Tilburg". Dit maakt het mogelijk om verschillende steden te configureren per website scraper.

## Hoe het werkt

### 1. Configuratie

In de `filtering_config` van een website configuratie kun je nu een `cities` array toevoegen:

```json
{
  "strategy_config": {
    "filtering_config": {
      "filters_container_selector": ".search-default",
      "cities": ["Amsterdam", "Rotterdam", "Utrecht", "Tilburg"]
    }
  }
}
```

### 2. Stad Selectie

- **Huidige gedrag**: De scraper gebruikt de **eerste stad** in de cities array
- **Fallback**: Als er geen cities geconfigureerd zijn, wordt "Tilburg" gebruikt (backwards compatibility)
- **Toekomst**: In de toekomst kan dit uitgebreid worden naar scraping van alle geconfigureerde steden

### 3. Backwards Compatibility

Bestaande configuraties zonder `cities` veld blijven gewoon werken:
- Ze gebruiken automatisch "Tilburg" als zoekstad
- Geen migratie van bestaande data nodig

## Configuratie Voorbeelden

### Nieuwe Configuratie met Steden

```json
{
  "website_identifier": "vesteda",
  "website_name": "Vesteda", 
  "strategy_config": {
    "filtering_config": {
      "filters_container_selector": ".search-default",
      "cities": ["Amsterdam", "Den Haag", "Rotterdam"]
    }
  }
}
```

In dit voorbeeld wordt "Amsterdam" gebruikt als zoekstad (eerste in de lijst).

### Bestaande Configuratie (werkt nog steeds)

```json
{
  "strategy_config": {
    "filtering_config": {
      "filters_container_selector": ".search-default"
    }
  }
}
```

Deze configuratie gebruikt automatisch "Tilburg" als zoekstad.

## Implementatie Details

### FilteringConfig Model

Het `FilteringConfig` Pydantic model is uitgebreid met:

```python
class FilteringConfig(BaseModel):
    filters_container_selector: Optional[str] = None
    js_code: Optional[str] = None
    filter_url_suffix: Optional[str] = None
    cities: Optional[List[str]] = None  # NIEUW
```

### BaseWebsiteScraper Methode

Nieuwe helper methode voor stad selectie:

```python
def _get_search_city(self) -> str:
    """
    Get the search city from filtering configuration.
    
    Returns:
        str: The city to use for searching. Falls back to "Tilburg" for backwards compatibility.
    """
    if (
        self.filtering_config 
        and self.filtering_config.cities 
        and len(self.filtering_config.cities) > 0
    ):
        return self.filtering_config.cities[0]
    return "Tilburg"
```

### JavaScript Template

De scrapers gebruiken nu dynamische JavaScript in plaats van hardcoded "Tilburg":

```javascript
const addressInput = searchContainer.querySelector('.search-field--adres input');
addressInput.value = '{search_city}';  // Dynamisch ingevuld
```

## Bestaande Configuratie Updaten

Om een bestaande configuratie te updaten met steden support:

1. **Via Script**: Gebruik `scripts/database/update_config_with_cities.py`
2. **Handmatig**: Update de JSON configuratie in de database
3. **Via API**: Update via de configuration management interface (als beschikbaar)

### Voorbeeld Script Gebruik

```bash
cd scripts/database
python update_config_with_cities.py
```

Dit script update de Vesteda configuratie met een lijst van Nederlandse steden.

## Toekomstige Uitbreidingen

### Multi-City Scraping per Run

In de toekomst kan de functionaliteit uitgebreid worden om:

1. **Alle steden in één run**: Loop over alle geconfigureerde steden
2. **Parallelle scraping**: Scrape meerdere steden tegelijkertijd  
3. **Stad-specifieke resultaten**: Houd resultaten per stad bij
4. **Configureerbare stad logica**: Verschillende scraping strategieën per stad

### Implementatie Voorbeeld (toekomstig)

```python
async def scrape_all_cities_async(self) -> Dict[str, List[House]]:
    """Scrape all configured cities and return results per city."""
    results = {}
    
    if self.filtering_config and self.filtering_config.cities:
        for city in self.filtering_config.cities:
            logger.info(f"Scraping city: {city}")
            # Set current city
            self.current_search_city = city
            # Run normal scraping process
            houses = await self.run_scrape_async()
            results[city] = houses
    
    return results
```

## Logging

De scrapers loggen nu welke stad wordt gebruikt:

```
INFO - Applying filters with search city: Amsterdam
```

Dit maakt debugging en monitoring eenvoudiger.

## Troubleshooting

### Probleem: Scraper gebruikt nog steeds "Tilburg"

**Oplossing**: 
1. Controleer of de `cities` array correct geconfigureerd is in de database
2. Controleer de logs voor "Applying filters with search city: ..."
3. Herstart de scraper na configuratie wijzigingen

### Probleem: Configuration parsing errors

**Oplossing**:
1. Valideer de JSON syntax van de configuratie
2. Zorg dat `cities` een array van strings is
3. Controleer de Pydantic model validatie logs

## Compatibiliteit

- **Python 3.8+**: Vereist voor List type hints
- **Pydantic v2**: Voor model validatie
- **SQLAlchemy**: Voor database configuratie opslag
- **Crawl4ai**: Voor web scraping functionaliteit 