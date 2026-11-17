# Number Guessing Game (CLI)

A command-line number guessing game built in Python as a learning project. It starts as a simple "guess the number" game and grows into a feature-rich terminal experience with difficulty levels, scoring, saved stats, and multiple game modes.

> **Status:** Work in progress. Features are added step by step, and the checklist below shows what's done.

## Features

- [x] Classic mode: guess the computer's number
- [x] Difficulty levels (easy, medium, hard) with limited attempts
- [x] Hot/cold hints based on how close your guess is
- [x] Input validation (no crashes on bad input)
- [x] Scoring based on attempts, difficulty, and time
- [ ] Win streak counter
- [ ] Persistent high-score leaderboard (saved to JSON)
- [ ] Player profiles and stats
- [ ] Reverse mode: the computer guesses your number using binary search
- [ ] Timed mode
- [ ] Two-player mode
- [ ] Daily challenge
- [x] Limited hints
- [ ] Achievements
- [ ] Colored output and menus

## Requirements

- Python 3.10 or newer

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/YOUR-USERNAME/number-guessing-game.git
   cd number-guessing-game
   ```

2. (Optional) Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install dependencies (once the project has any):

   ```bash
   pip install -r requirements.txt
   ```

4. Run the game:

   ```bash
   python game.py
   ```

## How to Play

1. Pick a difficulty level.
2. The computer chooses a secret number in that range.
3. Type your guess. After each guess you'll get a hint (higher, lower, or how close you are).
4. Guess the number before you run out of attempts.
5. Fewer attempts on harder levels means a higher score.

## Project Structure

```
number-guessing-game/
├── game.py          # Main entry point and game loop
├── storage.py       # Saving and loading scores and stats
├── ui.py            # Menus and display
├── stats.py         # Scoring and statistics
├── tests/           # Unit tests
├── requirements.txt
└── README.md
```

This layout will evolve as the project grows.

## Running Tests

```bash
pip install pytest
pytest
```

## Roadmap

See the feature checklist above. Ideas for later:

- Stats graphs of guess history
- Save and resume an unfinished game
- A simple AI opponent
- Packaging so it installs with `pip`

## What I'm Learning

This project is how I'm practicing Python: functions, classes, file handling, error handling, modules, testing, and Git/GitHub.

## License

This project is licensed under the MIT License.
