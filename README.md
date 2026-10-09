# Cinny support crew

A proof of concept of a customer support system for [Cinny](https://cinny.app), a movie and TV series tracking app. Three CrewAI agents read an incoming email, classify it, draft a reply from Cinny's documentation and review the reply before it is sent. Everything runs locally through Ollama.

Built as the project in D0058E.

## How it works

The crew runs three agents in sequence. Each task gets the output of the task before it.

| Agent | Task | Output |
|---|---|---|
| Triage Agent | Classifies the email | `CATEGORY` (SPAM, ACCOUNT, BUG, DATA_ERROR, FEEDBACK or OTHER), `SUMMARY`, `OTHER_ISSUES`, `REASON` |
| Response Agent | Writes a draft reply, using the RAG tool to look up facts | A reply email, or `NO_REPLY` for spam |
| Review Agent | Checks the draft and rewrites it if needed | The final email, or `NO_REPLY` |

Only the Response Agent has a tool, `cinny_knowledge_base`. It is a CrewAI `RagTool` that searches the Markdown files in `data/` and returns the 3 most relevant chunks.

## Requirements

- Python 3.13 and [uv](https://docs.astral.sh/uv/)
- [Ollama](https://ollama.com) running locally

## Setup

Install the dependencies:

```bash
uv sync
```

Download the models:

```bash
ollama pull llama3.2:3b
```

```bash
ollama pull nomic-embed-text-v2-moe
```

Only needed for the hierarchical process:

```bash
ollama pull qwen2.5:3b
```

Create a `.env` file from the example:

```bash
cp .env.example .env
```

```bash
OPENAI_API_BASE="http://localhost:11434/v1"
OPENAI_API_KEY="ollama"
OPENAI_MODEL_NAME="llama3.2:3b"
```

Ollama ignores the API key, but it must not be empty.

## Run

Run from the project root, since the documents are loaded with paths relative to it:

```bash
uv run .\src\main.py
```

This sends the test email in `main.py` through the crew and prints the final reply. More test emails, one per category, are in `src/test_emails.py`.

### Hierarchical process

The crew runs sequentially by default. To try the hierarchical process, uncomment these lines in `src/crew.py`:

```python
process=Process.hierarchical,
manager_agent=create_manager(),
```

The manager runs on `qwen2.5:3b`, because `llama3.2:3b` writes the delegation tool call as text instead of calling it. With these small models the hierarchical process does not get through all three agents.

## Project structure

```
data/                  Knowledge base for the RAG tool
  account-faq.md
  cinny-overview.md
  pricing-faq.md
  privacy-policy.md
  terms-and-conditions.md
src/
  main.py              Entry point, runs the crew on a test email
  crew.py              Builds the crew and the hierarchical manager
  agents.py            Agent definitions
  tasks.py             Task definitions and prompts
  tools.py             RAG tool setup
  llm.py               Ollama LLM config
  test_emails.py       Test emails, one per category
rapport.md             Project report
```

## Knowledge base

The documents in `data/` are embedded with `nomic-embed-text-v2-moe` and stored in ChromaDB. Chroma saves to disk under `%LOCALAPPDATA%\CrewAI\D0058E-project`, so the collection is cleared and rebuilt every time the tool is created. To change what the agent knows, edit the files in `data/` or the `doc_paths` list in `src/tools.py`.

## Known limitations

- `llama3.2:3b` sometimes makes up facts when the answer isn't in the retrieved chunks.
- It sometimes writes the tool call as text instead of calling the tool, so the search never runs.
- Spam is detected by the Triage Agent, but the Response Agent doesn't always respect `NO_REPLY`.
- Ollama runs `llama3.2:3b` with a 4096-token context. Long prompts get cut off from the start.

See `rapport.md` for the full evaluation.
