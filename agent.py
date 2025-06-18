from smolagents import CodeAgent
from smolagents import TransformersModel, LiteLLMModel


mode = "Ollama"  #Ollama works better LOL
if mode == "Transformers":
    MODEL_ID = "HuggingFaceTB/SmolLM-135M-Instruct"
    engine = TransformersModel(
        model_id=MODEL_ID,
        device_map="cuda",
        max_new_tokens=1000,
        do_sample=True,
        trust_remote_code=True
    )
elif mode == "Ollama":
    MODEL_ID = 'ollama_chat/gemma3:12b'
    engine = LiteLLMModel(
        model_id=MODEL_ID,
        api_base="http://127.0.0.1:11434",
        # api_key="your-api-key",
        num_ctx=8192
    )

from tools import (
    list_python_files,
    read_file,
    run_flake8,
    run_bandit,
    analyze_complexity
)

tools = [
    list_python_files,
    read_file,
    run_flake8,
    run_bandit,
    analyze_complexity
]

agent = CodeAgent(
    tools=tools,
    model=engine,
    additional_authorized_imports=[
        'os', 'subprocess', 'radon.complexity', 'open', 'ntpath'
    ]
)