import argparse
from agent import agent
from config import REPO_PATH


def run_analysis(path: str):
    prompt = (
        f"Analyze the Python project at '{path}' for performance, style, and security issues. "
        "Provide a structured report grouped by category and severity."
    )
    report = agent.run(prompt)
    print(report)


def main():
    parser = argparse.ArgumentParser(
        description='SmolAgents Python Codebase Analyzer'
    )
    parser.add_argument(
        '--path', '-p',
        default=REPO_PATH,
        help='Path to the Python repository to analyze'
    )
    args = parser.parse_args()
    run_analysis(args.path)


if __name__ == '__main__':
    main()