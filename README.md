# llama

## LlamaParse Setup (without exposing secrets)

[LlamaParse](https://github.com/run-llama/llama_parse) is a document parsing service by LlamaIndex. To use it securely, **never hardcode your API key** in your code. Use environment variables instead.

### 1. Install LlamaParse

```bash
pip install llama-parse
```

### 2. Set your API key

Copy `.env.example` to `.env` and add your key:

```bash
cp .env.example .env
```

Edit `.env`:

```
LLAMA_CLOUD_API_KEY=your_api_key_here
```

> **Important:** `.env` is listed in `.gitignore` and will **not** be committed. Never commit your real API key.

Get your API key at [https://cloud.llamaindex.ai/](https://cloud.llamaindex.ai/).

### 3. Load the environment variable in Python

```python
import os
from dotenv import load_dotenv
from llama_parse import LlamaParse

load_dotenv()  # loads variables from .env into os.environ

parser = LlamaParse(
    api_key=os.environ["LLAMA_CLOUD_API_KEY"],
    result_type="markdown",
)

documents = parser.load_data("your_document.pdf")
```

Install `python-dotenv` if you don't have it:

```bash
pip install python-dotenv
```

### Security checklist

- [x] API key stored in `.env`, not in source code
- [x] `.env` is in `.gitignore` — will never be committed
- [x] `.env.example` (no real values) is committed so teammates know what to configure