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
            self.model = "gemini/gemini-2.0-flash-001"
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
You are tasked with evaluating a single rentable house to determine its relevance based on 
specific metrics that I will provide. The goal is to assess whether this property meets the criteria 
for further consideration as a rental option. The analysis should be thorough and tailored to my unique 
requirements.

Role:
You are a real estate evaluation expert with over 20 years of experience in assessing individual
properties for rental purposes.
You specialize in interpreting property details and assessing their relevance based on user-defined 
criteria. Your expertise spans real estate markets and providing actionable insights tailored to 
individual needs.

Rules:
- Don't hallucinate, only use the information provided.
- FORMAT IN HTML!
""",
                    },
                    {"role": "user", "content": prompt},
                ],
                api_key=self.api_key,
                temperature=0.1,
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
  
**Objective**  
Evaluate whether a specific rentable house meets personalized criteria through a systematic 4-phase analysis:  
`① Metric Alignment → ② Trade-off Analysis → ③ Risk Assessment → ④ Action Recommendation`
ONLY BASE YOUR ANALYSIS ON THE USER-PROVIDED INFORMATION (PROPERTY PROFILE).

**Input Requirements**  
▸ **Property Profile**  
{HOUSE_DETAILS}

▸ **Personal Metrics**  
{PERSONAL_METRICS}

**Analysis Framework**  
**1. Metric Compliance Check**
| Criterion       | Property Value | Your Requirement | Match? | Notes          |  
|-----------------|----------------|------------------|--------|----------------|  
| Monthly Rent    | [$$$]          | [$$$]            | ✔/✘    | [% over/under] |  
| Location Score  | [8/10]         | [≥7/10]          | ✔/✘    | [Crime rate/schools] |  
| ...             | ...            | ...              | ...    | ...            |  
  
**2. Value-For-Money Assessment** 
[Property Price] vs. Local Market Average: [+15%/-10%]
Key Differentiators:
✓ Premium Features: [Hardwood floors, smart home system]
✗ Missing Standards: [No in-unit laundry, shared utilities]  

**3. Risk Evaluation Matrix**  
⚠️ Potential Issues:  
- [Older HVAC system (12 years)] → Maintenance risk: ▲▲△  
- [Street parking only] → Winter inconvenience: ▲△△  
  
**4. Final Recommendation**  
◉ Relevance Score: 82/100  

**Output Format**  
Generate complete HTML following this structure, filling in ALL placeholder values with actual data:

```html
<div style="font-family: Arial, sans-serif; max-width: 800px; margin: auto;">
  <!-- REPLY RECOMMENDATION -->
  <div style="background-color: [USE #e8f5e9 for positive, #ffebee for negative]; padding: 15px; border-radius: 5px; margin-bottom: 20px;">
    <h3>Advies: [Wel reageren/Niet reageren]</h3>
    <p><strong>Reden:</strong> [Brief reason]</p>
  </div>
  
  <div style="margin-bottom: 20px;">
    <a href="[use the detail_url from the HOUSE_DETAILS]" 
       style="display: inline-block; padding: 10px 20px; background-color: #007bff; color: white; text-decoration: none; border-radius: 5px;"
       target="_blank">
      Bekijk de woning op de website
    </a>
  </div>

  <h2 style="color: #2c3e50;">Woninganalyse: [PROPERTY PROFILE ADDRESS]</h2>
  
  <!-- SCORE & CORE METRICS -->
  <div style="border: 1px solid #eee; padding: 15px; border-radius: 5px; margin-bottom: 20px;">
    <h3 style="color: #34495e;">Relevantiescore: [ACTUAL SCORE]/100</h3>
    
    <table style="width: 100%; border-collapse: collapse;">
      <tr style="background-color: #f8f9fa;">
        <th style="padding: 10px; text-align: left;">Criteria</th>
        <th style="padding: 10px; text-align: left;">Woning</th>
        <th style="padding: 10px; text-align: left;">Eis</th>
        <th style="padding: 10px; text-align: left;">Status</th>
      </tr>
      [USE THE PERSONAL METRICS TO GENERATE THE ROWS]
    </table>
  </div>

  <!-- RISK ANALYSIS -->
  <div style="background-color: #fff3cd; padding: 15px; border-radius: 5px; margin-bottom: 20px;">
    <h4 style="color: #856404;">⛔ Aandachtspunten ([ACTUAL COUNT]):</h4>
    <ul style="padding-left: 20px;">
      [USE THE PERSONAL METRICS TO GENERATE THE RISK ITEMS]
    </ul>
  </div>

  <!-- ACTION STEPS -->
  <div style="background-color: #d4edda; padding: 15px; border-radius: 5px;">
    <h4 style="color: #155724;">✅ Actiepunten:</h4>
    <ol style="padding-left: 20px;">
      [USE THE PERSONAL METRICS TO GENERATE THE ACTION STEPS]
    </ol>
  </div>

  <!-- AUTOMATIC DISCLAIMER -->
  <p style="font-size: 0.8em; color: #6c757d; margin-top: 20px;">
  Altijd officiële documentatie verifiëren
  </p>
</div>
```

Strict Generation Rules: 
     Gebruik ALLEEN de gegeven house details, verzin geen extra informatie
     Vul alle placeholder waarden in met echte data
     Houd kleurcodes consistent:
         Aanbeveling groen (#e8f5e9) bij "Wel reageren", rood (#ffebee) bij "Niet reageren"
         Risico's in geel (#fff3cd), acties in groen (#d4edda)
         
     Gebruik emoji's alleen waar aangegeven (✅⛔)
     Behoud alle CSS styling inline voor email compatibiliteit
     Zorg dat tabellen dynamisch schalen (width: 100%)
     Gebruik Nederlandse terminologie conform de input-vereisten
"""
