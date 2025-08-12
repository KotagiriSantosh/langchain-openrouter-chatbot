LangChain + OpenRouter Chatbot (Python)

Build a lightweight **ChatGPT-style CLI chatbot** using **LangChain** and **OpenRouter**.  
No OpenAI billing required. Runs on any machine with Python.

https://github.com/ (add your repo link later)

---

✨ Features
- Real-time chat loop in the terminal
- Uses **OpenRouter** as a drop-in OpenAI-compatible API
- Switch models easily (GPT-3.5, GPT-4, Mistral, etc.)
- Clean, minimal code (~30 lines)
- Secure setup (no hardcoded keys)

---

🧱 Tech Stack
- **Python 3.10+** (tested on Windows 11)
- **LangChain** (`langchain-openai`)
- **OpenRouter** (OpenAI-compatible API)

---

📦 Quick Start

1) Create/OpenRouter API Key
1. Go to https://openrouter.ai/keys  
2. Click **Create Key** → copy the key (starts with `or-...`).

> ⚠️ **Keep your key private. Rotate immediately if you ever committed it.**

2) Set up a virtual environment (recommended)
**PowerShell (Windows):**
```powershell
py -m venv .venv
.venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

3) Install dependencies
```bash
pip install langchain langchain-openai
```

4) Configure your API key
**Option A – Environment variable (recommended)**
```powershell
Windows PowerShell
$env:OPENAI_API_KEY="or-xxxxxxxxxxxxxxxxxxxxxxxx"
```
```bash
macOS/Linux (bash/zsh)
export OPENAI_API_KEY="or-xxxxxxxxxxxxxxxxxxxxxxxx"
```

> We set `OPENAI_API_KEY` because the OpenAI-compatible client used by
> `langchain_openai` reads from this variable. (You can also pass the key
> directly in code via `api_key=`.)

5) Save the script as `chatbot.py`
```python
from langchain_openai import ChatOpenAI

Initialize model (reads OPENAI_API_KEY from env if not provided)
chat_model = ChatOpenAI(
    model="openai/gpt-3.5-turbo",
    openai_api_base="https://openrouter.ai/api/v1",
    # api_key="or-xxxxxxxx..."  # optional: pass explicitly instead of env var
)

print("🤖 OpenRouter Chatbot — type 'exit' to quit.
")

while True:
    query = input("You: ")
    if query.lower() in ["exit", "quit"]:
        print("AI: Goodbye! 👋")
        break

    try:
        response = chat_model.invoke(query)
        # response is a ChatMessage; print only the text content
        print("AI:", getattr(response, "content", response))
    except Exception as e:
        print("⚠️ Error:", e)
```

6) Run
```bash
python chatbot.py
```

---

🔁 Switch Models
Change the `model=` string to try different providers via OpenRouter:

| Friendly Name | Model ID (use in `model=`)       |
|---|---|
| GPT‑3.5 Turbo | `openai/gpt-3.5-turbo` |
| GPT‑4         | `openai/gpt-4`         |
| Mistral 7B    | `mistralai/mistral-7b-instruct` |
| Mixtral 8x7B  | `mistralai/mixtral-8x7b-instruct` |

> OpenRouter routes everything through the OpenAI Chat Completions API,
> so the same code path works across these models.

---

🔐 Security Notes
- **Never commit API keys**. Add this to `.gitignore`:
  ```gitignore
  .env
  *.env
  .venv/
  ```
- If you accidentally exposed a key, **revoke it** in your OpenRouter dashboard and create a new one.
- Prefer environment variables over hardcoding keys.

---

🧰 Troubleshooting

**`ModuleNotFoundError` / deprecated imports**  
Use the modern import:
```python
from langchain_openai import ChatOpenAI
```
Do **not** use `from langchain.chat_models import ChatOpenAI` (deprecated).

**429 / rate limit / insufficient quota**  
OpenRouter is free but can throttle. Try again later or switch to another model.

**401 Unauthorized**  
Check the key is set and correct:
```powershell
$env:OPENAI_API_KEY  # should print your or-... key
```

**Windows: multiple Pythons**  
Ensure you’re installing packages for the **same interpreter** you run with:
```powershell
C:/Path/To/Python/python.exe -m pip install langchain langchain-openai
C:/Path/To/Python/python.exe chatbot.py
```

---

🗺️ Roadmap (nice-to-haves)
- Streaming tokens (typing effect)
- Chat memory across turns
- Model picker menu
- Web UI (Streamlit/Gradio)

---



---

🤝 Credits
- OpenRouter (OpenAI-compatible API)
- LangChain team (`langchain-openai`)

---

**Made by:** Santosh Kotagiri  
*If you found this helpful, drop a ⭐ on the repo and connect with me!* 👍

