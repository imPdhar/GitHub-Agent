import argparse
from agent import agent
from config import REPO_PATH


def run_analysis(path: str):
    prompt = (
        f"Analyze the Python project at '{path}' for performance, style, and security issues. "
        "After it, do not forget to provide a structured report grouped by category and severity in the following format: \n"
        """Project Analysis Report:
        I. Style Issues:
        - Output gathered by flake8 (see full output for details).
        - Severity: Based on output gathered 

        II. Security Issues:
        - Bandit scan found X security vulnerabilities (where X is no or an integer number).
        - Severity: N/A or Mild or Severe 

        III. Performance Issues:
        - Tool used was (something).
        - Output gathered by the tool (see full output for details).

        IV. Complexity Analysis:
        - Automated complexity analysis and description.
        - Related comments."""
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
    print(args.path)
    run_analysis(args.path)


if __name__ == '__main__':
    main()