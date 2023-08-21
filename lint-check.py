import subprocess

import sys

# Define files to be checked

files_to_check = ["app.py"]

# Run linting checks using some linting tool (e.g., flake8)

for file_to_check in files_to_check:

	result = subprocess.run(["flake8", file_to_check], capture_output=True, text=True)

if result.returncode != 0:

	print(result.stdout)

	print(f"Linting failed for {file_to_check}")

sys.exit(1)
