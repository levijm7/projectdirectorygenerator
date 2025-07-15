import os
import shutil

dirs = ["assets",
        "bin",
        "ci",
        "configs",
        "contrib",
        "data",
        "data/raw",
        "data/processed",
        "data/results",
        "docs",
        "docs/architecture_diagrams",
        "docs/api",
        "docs/user_guide",
        "examples",
        "logs",
        "notebooks",
        "scripts",
        "tests",
        "src"]
files = ["docs/README.md",
         "logs/run-log.txt",
         "scripts/main_script.py",
         "tests/test_main.py",
         ".env.example",
         ".gitignore",
         "LICENSE",
         "requirements.txt",
         "CHANGELOG.md",
         "README.md"]

# Function to iterate through the list of directories and create them
def create_directories(directory_path, directories):
    for directory in directories:
        path = os.path.join(directory_path, directory)
        try:
            os.makedirs(path, exist_ok=True)
            print(f"Created directory: {path}")
        except Exception as e:
            print(f"Error creating directory {path}: {e}")

# Function to iterate through the list of files and create them
def create_files(directory_path, files):
    for file in files:
        path = os.path.join(directory_path, file)
        try:
            # Ensure the directory exists before creating the file
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, 'w') as f:
                f.write("")  # Create an empty file
            print(f"Created file: {path}")
        except Exception as e:
            print(f"Error creating file {path}: {e}")

def main():
    project_name = input("Enter the project name: ")
    directory_path = os.path.join(input("Enter the directory path where the project will be created: "), project_name)
    create_directories(directory_path, dirs)
    create_files(directory_path, files)
    # copy .devcontainer from projectdirectorygenerator to new project directory root
    devcontainer_src = os.path.join(os.path.dirname(__file__), "..", ".devcontainer")
    devcontainer_src = os.path.abspath(devcontainer_src)
    devcontainer_dst = os.path.join(directory_path, ".devcontainer")
    try:
        shutil.copytree(devcontainer_src, devcontainer_dst)
        print(f"Copied .devcontainer to: {devcontainer_dst}")
    except Exception as e:
        print(f"Error copying .devcontainer: {e}")
    #initialize git repository
    try:
        os.chdir(directory_path)
        os.system("git init")
        print(f"Initialized git repository in: {directory_path}")
    except Exception as e:
        print(f"Error initializing git repository: {e}")

if __name__ == "__main__":
    main()
    print("Project structure created successfully.")