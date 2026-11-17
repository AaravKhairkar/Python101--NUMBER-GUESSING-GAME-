#storage

import json
from pathlib import Path

DATA_FILE = Path(__file__).parent / "game_data.jsonl"


def adding_data(attempt_data):
    """Append one game record as one line."""
    with open(DATA_FILE, "a", encoding="utf-8") as file:
        file.write(json.dumps(attempt_data) + "\n")


def load_data():
    """Return a list of all saved game records."""
    if not DATA_FILE.exists():
        return []
    records = []
    with open(DATA_FILE, encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            try:
                records.append(json.loads(line))
            except json.JSONDecodeError:
                continue   # skip a damaged line instead of crashing
    return records