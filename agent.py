from smolagents import CodeAgent
from smolagents import TransformersModel
from transformers import pipeline

# Load a local model pipeline (e.g., StarCoder)
hf_pipeline = pipeline(
    'text-generation',
    model='bigcode/starcoder-base',
    device=-1
)
model = TransformersModel(pipeline=hf_pipeline)

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
    model=model,
    additional_authorized_imports=[
        'os', 'subprocess', 'radon.complexity'
    ]
)