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

    async def analyse_house(self, house: House) -> str:
        """Analyse a house using the LLM"""

        prompt = prompt_template.format(HOUSE_DETAILS=house.to_readable_string())

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

            content = response.choices[0].message.content

            if content == "null":
                return None

            return self.remove_markdown_block_syntax(content)
        except Exception as e:
            print(f"Error in {self.provider.value} extraction: {str(e)}")
            return None

    async def extract(
        self, markdown: str, schema: Dict[str, Any], provider: LLMProvider
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
                    DO NOT USE NEWLINE CHARACTERS (\\n) IN THE RETURNED JSON.
                    DO NOT USE MARKDOWN BLOCK SYNTAX (```json) IN THE RETURNED JSON.
                    THIS WILL CAUSE THE JSON.PARSE TO FAIL.
                    USE DOUBLE QUOTES FOR KEYS AND VALUES.
                    """,
                    },
                    {"role": "user", "content": markdown},
                ],
                api_key=api_key,
                temperature=0.1,
                response_format=schema,
            )

            content = response.choices[0].message.content # type: ignore

            if content == "null":
                return None

            return self.remove_markdown_block_syntax(content) # type: ignore
        except Exception as e:
            print(f"Error in {provider.value} extraction: {str(e)}")
            return None


prompt_template = """
**House Rental Relevance Analyzer**  
*(A Decision-Making Framework for Individual Property Evaluation)*  

**Objective**  
Evaluate whether a specific rentable house meets personalized criteria through a systematic 4-phase analysis:  
`① Metric Alignment → ② Trade-off Analysis → ③ Risk Assessment → ④ Action Recommendation`
ONLY BASE YOUR ANALYSIS ON THE USER-PROVIDED INFORMATION (PROPERTY PROFILE).
Don't make up any information, just use the information provided.

**Input Requirements**  
*(User-Provided Information)*  
▸ **Property Profile**  
   {HOUSE_DETAILS}

▸ **Personal Metrics**  
   - Budget: €1500/month
   - Location Priorities: Niet te ver uit de buurt van het centrum van Tilburg. Idealiter 10 minuten, maar als het iets langer is wil ik het ook weten. Een half uur is ECHT het maximum en heb ik liever niet.
   - Space Requirements: We hebben nu 40m2, en we willen er dus wel boven gaan zitten! Maar we willen vooral een plek die niet super heet of koud wordt. Bovenste verdieping van een flat is dan niet ideaal, tenzij het hele goede isolatie heeft. Vaak is dit niet af te lezen uit de gegeven huisgegevens helaas... 
   - Must-Have Features: Meer dan 40m2. Beschikbaar voor twee personen. Huur niet meer dan 1600
   - Nice-to-Have Features: Huisdieren toegestaan, vaatwasser

**Analysis Framework**

**1. Metric Compliance Check** 
| Criterion       | Property Value | Your Requirement | Match? | Notes          |  
|-----------------|----------------|------------------|--------|----------------|  
| Monthly Rent    | [$$$]          | [$$$]            | ✔/✘    | [% over/under] |  
| Location Score  | [8/10]         | [≥7/10]          | ✔/✘    | [Crime rate/schools] |  
| ...             | ...            | ...              | ...    | ...            |  

**2. Value-For-Money Assessment**  
```  
[Property Price] vs. Local Market Average: [+15%/-10%]  
Key Differentiators:  
✓ Premium Features: [Hardwood floors, smart home system]  
✗ Missing Standards: [No in-unit laundry, shared utilities]  
```

**3. Risk Evaluation Matrix**  
⚠️ Potential Issues:  
- [Older HVAC system (12 years)] → Maintenance risk: ▲▲△  
- [Street parking only] → Winter inconvenience: ▲△△  

**4. Final Recommendation**  
◉ Relevance Score: 82/100  

**Output Format**  
```markdown  
# [Property] Analysis Report  

## Executive Summary  
[TL;DR verdict with key highlights]  

## Detailed Breakdown  
### Core Requirements Match  
- [Metric 1]: ✔/✘ with [explanation]  
- [Metric 2]: ✔/✘ with [comparison]  

### Value Proposition  
✅ Advantages:  
- [Unique benefit 1]  
- [Cost-saving feature 2]  

⚠️ Limitations:  
- [Missing requirement 1]  
- [Premium pricing justification]  

### Action Plan  
1. Immediate Next Steps:  
   - [Contact landlord about X]  
   - [Verify Y documentation]  
2. Contingency Options:  
   - If [issue Z]: [Alternative solution]  
```

DON'T FORGET:
EVENTHOUGH WE'VE USED MARKDOWN SYNTAX, YOU MUST RETURN THE OUTPUT IN HTML.
ALSO, BEFORE THE ANALYSIS REPORT, YOU MUST RECOMMEND TO REPLY OR NOT REPLY TO THE RENTAL HOUSE
BECAUSE IT'S IMPORTANT TO BE THE FIRST TO SHOW INTEREST IN THE RENTAL HOUSE.
"""
