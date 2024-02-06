import subprocess
import os


def is_poetry_installed():
    try:
        subprocess.run(["poetry", "--version"],
                       check=True, stdout=subprocess.PIPE)
        return True
    except subprocess.CalledProcessError:
        return False


def is_pyproject_present():
    return os.path.exists("pyproject.toml")


def build_app():
    if not is_poetry_installed():
        print("poetry is not installed. Please install it first.")
        return

    if not is_pyproject_present():
        print("pyproject.toml not found. Ensure you are in the correct directory or that poetry is set up for this project.")

    cmd = [
        "poetry", "run", "pyinstaller", "--onefile",
        "--name=bricscad_version_checker",
        "--icon=icon.ico",
        "bricscad_version_checker\\main.py"
    ]

    # Execute the command
    subprocess.run(cmd)


if __name__ == "__main__":
    build_app()
