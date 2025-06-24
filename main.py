import argparse
from agent import agent
from config import REPO_PATH


def run_analysis(path: str):
    prompt = (
        f"Analyze the Python project at '{path}' for performance, style, and security issues. "
        "After it, do not forget to provide a structured report grouped by category and severity in the following format: \n"
        """Project Analysis Report:
        I. Style Issues:
        - Tell all issues found by flake8, grouped by severity)
        - Severity: None or Mild or Severe  (Based on output gathered)

        II. Security Issues:
        - Bandit scan found X security vulnerabilities (where X is no or an integer number).
        - Severity: None or Mild or Severe 

        III. Performance Issues:
        - Tool used was (something).
        - Output gathered by the tool (see full output for details).

        IV. Complexity Analysis:
        - Automated complexity analysis and description.
        - Related comments.

        V. Suggested code changes:
        - Change this to this (where this is the suggested code change) in file X.py: (where X is the file name) to improve performance, style, or security.
        - Change this to this (where this is the suggested code change) in file Y.py: (where Y is the file name) to improve performance, style, or security.
        - Change this to this (where this is the suggested code change) in file Z.py: (where Z is the file name) to improve performance, style, or security.
        and so on for all the files in the project.       
        """
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