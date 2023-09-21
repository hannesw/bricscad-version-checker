import subprocess
import os

def is_pipenv_installed():
    try:
        subprocess.run(["pipenv", "--version"], check=True, stdout=subprocess.PIPE)
        return True
    except subprocess.CalledProcessError:
        return False

def is_pipfile_present():
    return os.path.exists("Pipfile")

def build_app():
    if not is_pipenv_installed():
        print("pipenv is not installed. Please install it first.")
        return

    if not is_pipfile_present():
        print("Pipfile not found. Ensure you are in the correct directory or that pipenv is set up for this project.")
        return

    cmd = [
        "pipenv", "run", "pyinstaller", "--onefile",
        "--name=bricscad_version_checker",
        "--icon=icon.ico",
        "main.py"
    ]


    # Execute the command
    subprocess.run(cmd)

if __name__ == "__main__":
    build_app()
