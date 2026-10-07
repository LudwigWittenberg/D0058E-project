import os
from crewai import LLM
from dotenv import load_dotenv

load_dotenv()

# Explicit LLM so CrewAI doesn't fall back to real OpenAI. Ollama exposes an
# OpenAI-compatible API ("openai/" prefix) and ignores the key, but the SDK
# rejects an empty one, hence the "ollama" dummy fallback.
llm = LLM(
    model=f"openai/{os.getenv('OPENAI_MODEL_NAME', 'llama3.2:3b')}",
    base_url=os.getenv("OPENAI_API_BASE", "http://localhost:11434/v1"),
    api_key=os.getenv("OPENAI_API_KEY") or "ollama",
)