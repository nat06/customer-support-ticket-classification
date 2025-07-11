from pydantic import BaseModel


class Settings(BaseModel):
    mistral_api_key: str
    mistral_model: str = "ministral-3b-2410"
    fewshot_examples: int = 3
    output_dir: str = "outputs/"
