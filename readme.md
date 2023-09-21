# Bricscad Version Checker

This repository contains a Python script that checks the current version of Bricscad from their website and compares it with a previously stored version. If there's a change in the version, the user is notified, and the new version is stored locally.

## Features:

1. **Locale-Aware**: The script fetches the release notes based on the system's default locale setting.
2. **Notification**: Uses `tkinter` to display a notification message to the user about the version status.
3. **Persistent Storage**: Stores the currently checked version in a local JSON file.

## Usage:

Simply run the standalone executable. If it's your first time running the application, it will fetch the current version of Bricscad from the web and store it. On subsequent runs, it will compare the web version with the stored version and notify you if there's a change.

## Advanced Usage:

In addition to the default behavior, you can also use the following command-line option:

- **`--show-always`**: By default, the script will only notify you if the Bricscad version has changed from the stored version. Use this flag to always show the current version, regardless of any changes:

  ```bash
  dist/bricscad_version_checker.exe --show-always
  ```

# Development

## Prerequisites:

- Python 3.x
- pipenv
- PyInstaller
- Additional Python packages as specified in the `Pipfile`.

## Setup:

```bash
git clone https://github.com/hannesw/bricscad-version-checker.git
cd bricscad-version-checker
pipenv install
```

## Build:

You can create a standalone executable of this script for easy distribution and usage. We use PyInstaller for this purpose.

1. Run the build script:

   ```bash
   python build.py

   ```

   This command will generate a single executable file named bricscad_version_checker.exe with an associated icon.

2. Execute the standalone application:
   ```bash
   dist/bricscad_version_checker.exe
   ```

## Testing

This application includes unit tests to ensure its core functionalities. To run the tests:

```bash
pipenv install --dev
python test_main.py
```
