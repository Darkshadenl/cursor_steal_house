import re
from typing import Any, Dict, Optional
from litellm import acompletion, completion
import os
from dotenv import load_dotenv
from enum import Enum

load_dotenv()

class LLMProvider(Enum):
    DEEPSEEK = "deepseek"
    GEMINI = "gemini"

class LLMService:
    def __init__(self):
        self.deepseek_api_key = os.getenv("DEEPSEEK_API_KEY")
        self.google_api_key = os.getenv("GOOGLE_API_KEY")
        
    def remove_markdown_block_syntax(self, markdown: str) -> str:
        """Remove markdown block syntax + newlines from markdown string"""
        # First remove any markdown block syntax (```json, ```, etc)
        markdown = re.sub(r'^```.*\s*', '', markdown, flags=re.MULTILINE)
        # Then remove any remaining newlines
        return markdown.replace('\n', '')
    
    async def extract(self, markdown: str, schema: Dict[str, Any], provider: LLMProvider) -> Optional[Dict[str, Any]]:
        """Extract structured data from markdown using specified LLM provider"""
        try:
            if provider == LLMProvider.DEEPSEEK:
                model = "deepseek/deepseek-chat"
                api_key = self.deepseek_api_key
            elif provider == LLMProvider.GEMINI:
                model = "gemini/gemini-2.0-flash-001"
                api_key = self.google_api_key
            else:
                raise ValueError(f"Unsupported LLM provider: {provider}")
                
            response = await acompletion(
                model=model,
                messages=[{
                    "role": "system",
                    "content": f"""
                    Extract structured data from the given information.
                    The JSON you return must match the schema exactly.
                    {schema}
                    If you can't find the data, return null.
                    **IMPORTANT**
                    DO NOT USE NEWLINE CHARACTERS (\\n) IN THE RETURNED JSON.
                    DO NOT USE MARKDOWN BLOCK SYNTAX (```json) IN THE RETURNED JSON.
                    THIS WILL CAUSE THE JSON.PARSE TO FAIL.
                    USE DOUBLE QUOTES FOR KEYS AND VALUES.
                    """
                }, {
                    "role": "user",
                    "content": markdown
                }],
                api_key=api_key,
                temperature=0.1,
                response_format=schema
            )
            return self.remove_markdown_block_syntax(response.choices[0].message.content)
        except Exception as e:
            print(f"Error in {provider.value} extraction: {str(e)}")
            return None 