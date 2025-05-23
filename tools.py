import os
import subprocess
from radon.complexity import cc_visit
from smolagents import tool

@tool
def list_python_files(directory: str) -> list[str]:
    """List all Python files in the given directory (recursively)."""
    file_paths = []
    for root, _, files in os.walk(directory):
        for fname in files:
            if fname.endswith('.py'):
                file_paths.append(os.path.join(root, fname))
    return file_paths

@tool
def read_file(path: str) -> str:
    """Read and return the contents of the file at the given path."""
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

@tool
def run_flake8(directory: str) -> str:
    """Run flake8 linter on the directory and return summary of issues."""
    result = subprocess.run([
        'flake8', directory, '--statistics', '--exit-zero'
    ], capture_output=True, text=True)
    return result.stdout

@tool
def run_bandit(directory: str) -> str:
    """Run Bandit security analyzer on the directory and return the report."""
    result = subprocess.run([
        'bandit', '-r', directory, '-q', '-f', 'json'
    ], capture_output=True, text=True)
    return result.stdout or 'No issues found.'

@tool
def analyze_complexity(path: str) -> dict:
    """Compute cyclomatic complexity metrics for the given file."""
    code = ''
    with open(path, 'r', encoding='utf-8') as f:
        code = f.read()
    results = cc_visit(code)
    return {item.name: item.complexity for item in results}