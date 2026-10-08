from crewai_tools import RagTool
from crewai_tools.tools.rag import RagToolConfig, ProviderSpec
from pydantic import BaseModel, Field

COLLECTION_NAME = "cinny-collection"

def rag_tool():
  embedding_model: ProviderSpec = {
    "provider": "ollama",
    "config": {
      "model_name": "nomic-embed-text-v2-moe",
      "url": "http://localhost:11434/api/embeddings"
    }
  }

  # Chroma is the default vector DB. The collection name is a RagTool field,
  # not part of the vectordb config
  config: RagToolConfig = {
    "embedding_model": embedding_model
  }

  # The agent only sees name + description when deciding whether to use the tool;
  # the RagTool default is too generic, so spell out when it must be used
  tool = RagTool(
    config=config,
    collection_name=COLLECTION_NAME,
    limit=3, # Dont fill the whole count
    name="cinny_knowledge_base",
    description=(
      "Search Cinny's official FAQ and documentation. "
      "ALWAYS use this before answering any customer question about Cinny, "
      "e.g. pricing, Cinny Plus, account, data export, deletion, features or supported devices. "
      "Search once per question. If it returns nothing relevant, the answer is unknown: do not guess."
    ),
  )

  # Clear the collection.
  client = tool.adapter._client
  client.delete_collection(collection_name=COLLECTION_NAME)
  client.get_or_create_collection(collection_name=COLLECTION_NAME)

  # Documents
  doc_paths = [
    "data/cinny-overview.md",
    "data/pricing-faq.md",
    "data/account-faq.md",
    "data/privacy-policy.md",
    "data/terms-and-conditions.md",
  ]

  for doc_path in doc_paths:
    tool.add(data_type="file", path=doc_path)

  return tool
