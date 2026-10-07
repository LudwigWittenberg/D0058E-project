from crewai import LLM
from dotenv import load_dotenv

load_dotenv()

llm = LLM(
    model=f"openai/{os.getenv('OPENAI_MODEL_NAME', 'llama3.2:3b')}",
    base_url=os.getenv("OPENAI_API_BASE", "http://localhost:11434/v1"),
    api_key=os.getenv("OPENAI_API_KEY") or "ollama",
)