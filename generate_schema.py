import os
from crawl4ai.extraction_strategy import (
    JsonCssExtractionStrategy,
    JsonXPathExtractionStrategy,
)
from crawl4ai import LLMConfig
from dotenv import load_dotenv

load_dotenv()

name = "test_gallery_schema"
html = open(f"{name}.html", "r").read()
if 'gallery' in name:
    query_text = """ 
    In de gegeven html staat maar een deel van de gehele pagina.
    Het is een pagina met een gallerij van huurwoningen.
    """
else:
    query_text = """
    In de gegeven html staat maar een deel van de gehele pagina.
    Het is een pagina met informatie over een woning die verhuurd wordt.
    Ik ben geïnteresseerd in alle informatie over de woning.
    """


google = os.getenv("GOOGLE_API_KEY")

css_schema = JsonCssExtractionStrategy.generate_schema(
    html,
    schema_type="XPATH",
    query="""
    Let op! {query_text}
    Ik ben voor mijn database opzoek naar deze gegevens. Probeer dus dit soort gegevens te vinden:
    address, city, postal_code, neighborhood, status, high_demand, demand_message, detail_url, rental_price, service_costs, min_income_single, min_income_joint, read_more_url, square_meters, bedrooms, energy_label, available_from, complex, complex_name, complex_description, year_of_construction, number_of_objects, number_of_floors, description, location_map_url, request_viewing_url, options, is_parkingspot
    """,
    llm_config=LLMConfig(provider="gemini/gemini-2.0-flash-001", api_token=google),
)

# Use the generated schema for fast, repeated extractions
strategy = JsonCssExtractionStrategy(css_schema)

print(strategy.schema)
