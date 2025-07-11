import os

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

# Function to ask user for project name
def get_project_name():
    project_name = input("Enter the project name: ")
    return project_name

#Function to ask user for directory path
def get_directory_path(project_name):
    directory_path = input("Enter the directory path where the project will be created: ")
    return os.path.join(directory_path, project_name)

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

if __name__ == "__main__":
    project_name = get_project_name()
    directory_path = get_directory_path(project_name)
    create_directories(directory_path, dirs)
    create_files(directory_path, files)