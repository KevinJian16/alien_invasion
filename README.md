# Alien Invasion (Python / pygame-ce)

A small Python game built with pygame-ce.
Press P or Click "Start" to play.
Press Q to exit.

## Requirements

- Python 3.11+
- pygame-ce 2.5.6

## How to run

1. Clone the repo:

   git clone <YOUR_REPO_URL>
   cd <YOUR_REPO_FOLDER>

2. Create a virtual environment:

   python -m venv .venv

3. Activate the virtual environment:

   macOS / Linux:

   source .venv/bin/activate

   Windows (PowerShell):

   .\.venv\Scripts\Activate.ps1

4. Install dependencies and run:

   pip install -r requirements.txt
   python main.py

## Project structure

- main.py: entry point
- images/: assets
- other *.py files: game modules (ship, bullets, settings, etc.)

## Notes

- The .venv/ folder is not committed to Git.
- If you see import errors, ensure the venv is activated and dependencies are installed.
