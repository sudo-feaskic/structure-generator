import os

def structure_generator(start_path):
    for root, dirs, files in os.walk(start_path):

        if any(excluded in root for excluded in ['venv', '.git', '__pycache__']):
            continue

        dirs[:] = [d for d in dirs if d not in ['venv', '.git', '__pycache__']]

        level = root.replace(start_path, '').count(os.sep)
        indent = ' ' * 4 * level
        print(f"{indent}{os.path.basename(root)}/")

        for file in files:
            if file == '.gitignore':
                continue
            print(f"{indent}    ├── {file}")

project_path = os.getcwd()
structure_generator(project_path)
