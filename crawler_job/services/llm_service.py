import re
from typing import Any, Dict, Optional
from litellm import acompletion
import os
from dotenv import load_dotenv
from enum import Enum

from crawler_job.models.house_models import House

load_dotenv()


class LLMProvider(Enum):
    DEEPSEEK = "deepseek"
    GEMINI = "gemini"


class LLMService:
    def __init__(self, provider: LLMProvider = LLMProvider.DEEPSEEK):
        self.deepseek_api_key = os.getenv("DEEPSEEK_API_KEY")
        self.google_api_key = os.getenv("GOOGLE_API_KEY")

        self.model = "deepseek/deepseek-chat"
        self.api_key = self.deepseek_api_key

        if provider == LLMProvider.GEMINI:
            self.model = "gemini/gemini-2.5-flash"
            self.api_key = self.google_api_key

    def remove_markdown_block_syntax(self, markdown: str) -> str:
        """Remove markdown block syntax + newlines from markdown string"""
        # First remove any markdown block syntax (```json, ```, etc)
        markdown = re.sub(r"^```.*\s*", "", markdown, flags=re.MULTILINE)
        # Then remove any remaining newlines
        return markdown.replace("\n", "")

    async def analyse_house(
        self, house: House, personal_metrics: Optional[str] = None
    ) -> str:
        """Analyse a house using the LLM"""

        house_readable_string = house.to_readable_string()

        prompt = prompt_template.format(
            HOUSE_DETAILS=house_readable_string,
            PERSONAL_METRICS=personal_metrics or "No personal metrics provided.",
        )

        try:
            response = await acompletion(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": """
You are tasked with evaluating a single rentable house to determine its relevance and suitability as a rental option, based on specific personal metrics provided by the user. The goal is to deliver a balanced, nuanced assessment that weighs must-have criteria against nice-to-have preferences, identifies trade-offs, and provides actionable recommendations. Focus on real-world practicality: for example, if a user's budget is tight (e.g., €850/month), prioritize affordability and functional space over luxury ideals, recognizing that a studio can meet "space requirements" by offering a versatile living area even without separate rooms. Your analysis should be thorough, empathetic to the user's unique situation, and tailored to encourage informed decisions rather than hasty rejections.

Role:
You are a seasoned real estate evaluation expert with over 20 years of hands-on experience in scouting and assessing rental properties across diverse markets. You've advised everyone from budget-strapped students to growing families, specializing in interpreting property details through a human lens—balancing hard data with lifestyle fit, market realities, and clever compromises. Your insights are sharp, practical, and optimistic where opportunities shine, drawing on deep knowledge of local trends (e.g., Tilburg's centrality and transport quirks) to provide tailored, empowering advice that highlights potential wins amid imperfections.

Rules:
- Base your analysis exclusively on the user-provided information (property profile and personal metrics)—do not hallucinate, invent, or assume additional details.
- Differentiate clearly between must-have criteria (e.g., strict budget caps like €850/month or minimum bedrooms) and nice-to-have features (e.g., dishwasher or balcony), allowing flexibility in the latter to avoid overly negative assessments.
- Conduct a balanced evaluation: consider trade-offs, such as longer commute times if other factors excel, or compact spaces that still offer functional living for the user's needs.
- Think humanly and contextually—e.g., for a solo renter seeking 40m² with a place to sit, a studio is often ideal despite no separate bedroom; for a family needing 2 bedrooms, emphasize room count but note if adjacent spaces could adapt.
- Structure your response using a systematic framework: 1) Metric Compliance Check (table-based), 2) Value-for-Money and Trade-off Assessment, 3) Risk Evaluation, 4) Final Recommendation with a holistic relevance score (0-100, favoring higher scores for viable options).
- FORMAT YOUR ENTIRE OUTPUT IN HTML! Use the provided template structure where applicable, ensuring inline CSS for compatibility, dynamic tables, and consistent color-coding (green for positives, red for negatives, yellow for risks). Include elements like recommendation blocks, tables for metrics, lists for risks/actions, and a link to the property details.
- Always end with a brief, automatic disclaimer in small text: "Altijd officiële documentatie verifiëren."
""",
                    },
                    {"role": "user", "content": prompt},
                ],
                api_key=self.api_key,
                temperature=0.1,
                reasoning_effort=(
                    "low" if self.model == "gemini/gemini-2.5-flash" else None
                ),
            )

            content = response.choices[0].message.content  # type: ignore

            if content == "null":
                return None  # type: ignore

            return self.remove_markdown_block_syntax(content)  # type: ignore
        except Exception as e:
            print(f"Error in {self.model} extraction: {str(e)}")
            return None  # type: ignore

    async def extract(
        self,
        markdown: str,
        schema: Dict[str, Any],
        provider: LLMProvider,
        extra_instructions: Optional[str] = None,
    ) -> Optional[Dict[str, Any]]:
        """Extract structured data from markdown using specified LLM provider"""
        try:
            if provider == LLMProvider.DEEPSEEK:
                model = "deepseek/deepseek-chat"
                api_key = self.deepseek_api_key
            elif provider == LLMProvider.GEMINI:
                model = "gemini/gemini-2.0-flash-001"
                api_key = self.google_api_key

            response = await acompletion(
                model=model,
                messages=[
                    {
                        "role": "system",
                        "content": f"""
                    Extract structured data from the given information.
                    The JSON you return must match the schema exactly.
                    {schema}
                    If you can't find the data, return a simple string 'null'.
                    **IMPORTANT**
                    - DO NOT USE NEWLINE CHARACTERS (\\n) IN THE RETURNED JSON.
                    - DO NOT USE MARKDOWN BLOCK SYNTAX (```json) IN THE RETURNED JSON.
                    - THIS WILL CAUSE THE JSON.PARSE TO FAIL.
                    - USE DOUBLE QUOTES FOR KEYS AND VALUES.
                    
                    
                    Extra instructions, if any:
                    {extra_instructions}
                    """,
                    },
                    {"role": "user", "content": markdown},
                ],
                api_key=api_key,
                temperature=0.1,
                response_format=schema,
            )

            content = response.choices[0].message.content  # type: ignore

            if content == "null":
                return None

            return self.remove_markdown_block_syntax(content)  # type: ignore
        except Exception as e:
            print(f"Error in {provider.value} extraction: {str(e)}")
            return None


prompt_template = """
**House Rental Relevance Analyzer**  
_(A Decision-Making Framework for Individual Property Evaluation)_  

**Input Requirements**  
▸ **Property Profile**  
{HOUSE_DETAILS} 

▸ **Personal Metrics**  
{PERSONAL_METRICS}

**Analysis Framework**  
**1. Metric Alignment Check**  
Compare the property against user metrics, prioritizing must-haves (e.g., budget, bedrooms) over nice-to-haves. Use a table to show:  
| Criterion | Property Value | User Requirement | Fit (Full/Partial/None) | Notes |  
|----------|----------------|------------------|-------------------------|-------|  
| Monthly Rent | [$$$] | [$$$] | [Full/Partial/None] | [e.g., 5% over budget, negotiable?] |  
| Location | [Distance/Time] | [e.g., ≤30min to center] | [Full/Partial/None] | [e.g., 25min by bike, good transit] |  
| Space | [m²/rooms] | [e.g., ~40m²] | [Full/Partial/None] | [e.g., Studio, functional layout] |  
Generate rows dynamically from user metrics, noting partial fits (e.g., 38m² for a 40m² request is “Partial” but viable).  

**2. Value-for-Money and Trade-off Assessment**  
Compare the property’s rent to the local market average (e.g., Tilburg studio ~€800, 2-bedroom ~€1200). Highlight:  
✓ Premium Features: [e.g., modern kitchen, pet-friendly]  
✗ Trade-offs: [e.g., no balcony, but spacious living area]  
Assess if trade-offs align with user priorities (e.g., budget over luxury for €850 user).  

**3. Risk Evaluation Matrix**  
Identify potential issues, scoring their impact (Low/Medium/High) and likelihood based on user concerns:  
- [e.g., Older HVAC (12 years)] → Maintenance risk: Medium, likely  
- [e.g., Street parking] → Inconvenience: Low, certain  
List 0-5 risks, prioritizing those tied to must-haves (e.g., budget risks over aesthetic ones). If none, state: “No major concerns.”  

**4. Action Recommendation**  
Assign a relevance score (0-100, weighted toward must-haves: e.g., budget/location 60%, space/features 40%). Recommend one of:  
- **Strongly Recommend**: Score 80-100, meets most must-haves, minor trade-offs.  
- **Consider with Negotiation**: Score 60-79, meets key must-haves but needs fixes (e.g., negotiate rent).  
- **Pass Unless Specific Fixes**: Score <60, misses critical must-haves but could work with changes.  
Justify with a brief reason tied to trade-offs and user priorities.  

**Output Format**  
Generate complete HTML following this structure, filling ALL placeholders with data from HOUSE_DETAILS and PERSONAL_METRICS:  

```html
<div style="font-family: Arial, sans-serif; max-width: 800px; margin: auto;">
  <!-- RECOMMENDATION -->
  <div style="background-color: [Strongly Recommend: #e8f5e9; Consider: #fff3cd; Pass: #ffebee]; padding: 15px; border-radius: 5px; margin-bottom: 20px;">
    <h3>Advies: [Strongly Recommend/Consider with Negotiation/Pass Unless Specific Fixes]</h3>
    <p><strong>Reden:</strong> [e.g., Meets budget and location, lacks balcony but spacious]</p>
  </div>
  
  <div style="margin-bottom: 20px;">
    <a href="[detail_url from HOUSE_DETAILS]" 
       style="display: inline-block; padding: 10px 20px; background-color: #007bff; color: white; text-decoration: none; border-radius: 5px;"
       target="_blank">
      Bekijk de woning op de website
    </a>
  </div>

  <h2 style="color: #2c3e50;">Woninganalyse: [PROPERTY ADDRESS]</h2>
  
  <!-- SCORE & METRICS -->
  <div style="border: 1px solid #eee; padding: 15px; border-radius: 5px; margin-bottom: 20px;">
    <table style="width: 100%; border-collapse: collapse;">
      <tr style="background-color: #f8f9fa;">
        <th style="padding: 10px; text-align: left;">Criteria</th>
        <th style="padding: 10px; text-align: left;">Woning</th>
        <th style="padding: 10px; text-align: left;">Prioriteit</th>
        <th style="padding: 10px; text-align: left;">Fit</th>
        <th style="padding: 10px; text-align: left;">Opmerkingen</th>
      </tr>
      [Dynamically generate rows from PERSONAL_METRICS]
    </table>
  </div>

  <!-- RISK ANALYSIS -->
  <div style="background-color: #fff3cd; padding: 15px; border-radius: 5px; margin-bottom: 20px;">
    <h4 style="color: #856404;">⛔ Aandachtspunten ([COUNT]):</h4>
    <ul style="padding-left: 20px;">
      [List risks with impact/likelihood, or “Geen grote zorgen” if none]
    </ul>
  </div>

  <!-- ACTION STEPS -->
  <div style="background-color: #d4edda; padding: 15px; border-radius: 5px;">
    <h4 style="color: #155724;">✅ Actiepunten:</h4>
    <ol style="padding-left: 20px;">
      [Generate 1-3 steps, e.g., “Contact landlord to negotiate rent,” “Verify transit to center”]
    </ol>
  </div>

  <!-- DISCLAIMER -->
  <p style="font-size: 0.8em; color: #6c757d; margin-top: 20px;">
    Controleer altijd de officiële documentatie voordat u een beslissing neemt.
  </p>
</div>
"""
