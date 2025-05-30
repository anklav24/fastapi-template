import subprocess

commands = [
    "ruff check --fix",
    "ruff check --select I --fix",
    "ruff format",
    "mypy app",
    "python -m pytest --cov app --cov-fail-under=80 tests",
]

for command in commands:
    result = subprocess.run(command, shell=True)
    if result.returncode != 0:
        print(f"Command '{command}' failed with return code {result.returncode}")
        break
