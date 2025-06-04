from smolagents import CodeAgent
from smolagents import TransformersModel, LiteLLMModel
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import torch


mode = "Ollama"  # or "LiteLLM"
# MODEL_ID = "HuggingFaceTB/SmolLM2-1.7B-Instruct"
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
    MODEL_ID = 'ollama_chat/llama3.2:3b'
    engine = LiteLLMModel(
        model_id=MODEL_ID,
        api_base="http://127.0.0.1:11434",
        # api_key="your-api-key",
        num_ctx=8192
    )

# tokenizer = AutoTokenizer.from_pretrained(MODEL_ID, trust_remote_code=True)
# model     = AutoModelForCausalLM.from_pretrained(
#     MODEL_ID,
#     device_map="cuda",            # GPU if available
#     torch_dtype="auto"            # fp16 / bf16 when possible
# )

# hf_pipeline = pipeline(
#     "text-generation",
#     model=model,
#     tokenizer=tokenizer,
#     max_new_tokens=1024,
#     do_sample=True,
#     temperature=0.2
# )

# engine = TransformersModel(pipeline=hf_pipeline)
# engine = TransformersModel(
#     model_id=MODEL_ID,
#     device_map="cuda",
#     max_new_tokens=1000,
#     do_sample=True,
#     trust_remote_code=True
# )

# Import your tools
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
        'os', 'subprocess', 'radon.complexity', 'open'
    ]
)