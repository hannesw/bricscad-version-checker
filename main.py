import os
import json
import requests
import locale
import argparse
from bs4 import BeautifulSoup

# Conditionally import tkinter to enable headless testing
USE_GUI = os.environ.get('USE_GUI', 'True').lower() == 'true'
if USE_GUI:
    from tkinter import messagebox


HOME_DIR = os.path.expanduser("~")
FILE_PATH = os.path.join(HOME_DIR, 'bricscad_version.json')

def get_system_locale():
    # Get the system's locale, e.g., 'de_DE'
    loc = locale.getlocale()[0]
    if loc:
        return loc
    else:
        # Return a default value if the locale can't be determined
        return 'en_US'


def fetch_version_from_web():
    lang = get_system_locale()
    url = f'https://boa.bricsys.com/common/releasenotes.jsp?l={lang}'
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    version_tag = soup.find('h1', class_='version')
    if version_tag:
        return version_tag.text.strip()
    else:
        raise Exception("Couldn't find the version information on the webpage.")

def read_stored_version():
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, 'r') as file:
            data = json.load(file)
            return data['version']
    return None

def write_version_to_disk(version):
    with open(FILE_PATH, 'w') as file:
        json.dump({'version': version}, file)

def main():
    parser = argparse.ArgumentParser(description="Bricscad Version Checker")
    parser.add_argument("--show-always", action="store_true",
                        help="Always show the current version, regardless of any changes.")
    args = parser.parse_args()

    web_version = fetch_version_from_web()
    stored_version = read_stored_version()

    if stored_version is None or args.show_always:
        write_version_to_disk(web_version)
        if USE_GUI:
            messagebox.showinfo('Bricscad Version', f'The current Bricscad version is: {web_version}. Stored to disk.')
    elif stored_version != web_version:
        write_version_to_disk(web_version)
        if USE_GUI:
            messagebox.showinfo('Bricscad Version', f'Bricscad version has changed from {stored_version} to {web_version}. Updated on disk.')

if __name__ == '__main__':
    main()