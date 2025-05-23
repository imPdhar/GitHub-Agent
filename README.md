# SmolAgents Python Codebase Analyzer

**Overview:**
A local CLI tool that uses a Hugging Face SmolAgents LLM agent to analyze a Python codebase for performance bottlenecks, style issues (PEP8), and security vulnerabilities.

## Installation
```bash
pip install -r requirements.txt
```

## Usage
```bash
python main.py --path /path/to/your/repo
```

The agent will print a structured report summarizing issues by category and severity.