from mistralai import Mistral
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("MISTRAL_API_KEY")

client = Mistral(api_key=API_KEY)


def LLM_call(prompt: str, model: str = "mistral-medium-2505") -> str:
    response = client.chat.complete(
        model=model,
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content.strip()
