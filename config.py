REPO_PATH = './myrepo'

# Model identifier (local or HF API)
MODEL_ID = 'bigcode/starcoder-base'

# Linter commands
FLAKE8_ARGS = ['--statistics', '--exit-zero']

# Bandit arguments
BANDIT_ARGS = ['-r', '-q', '-f', 'json']

# Agent categories and severities settings (optional extension)
CATEGORY_SEVERITIES = {
    'performance': ['High', 'Medium', 'Low'],
    'style': ['Medium', 'Low'],
    'security': ['High', 'Medium', 'Low']
}