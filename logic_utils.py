from typing import Literal

DIFFICULTY_OPTIONS = {"Easy": (1, 20), "Normal": (1, 50), "Hard": (1, 100)}


def get_range_for_difficulty(difficulty: str):
    if difficulty not in DIFFICULTY_OPTIONS:
        raise ValueError(f"Invalid difficulty level: {difficulty}")
    return DIFFICULTY_OPTIONS.get(difficulty)


def parse_guess(raw: str, low: int, high: int):
    if not raw:
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    if value < low or value > high:
        return False, None, f"Guess must be between {low} and {high}."

    return True, value, None


def check_guess(guess: int, secret: int):
    if guess == secret:
        return "Win", "🎉 Correct!"

    if guess > secret:
        return "Too High", "📉 Go LOWER!"
    else:
        return "Too Low", "📈 Go HIGHER!"


def update_score(
    current_score: int,
    outcome: Literal["Win", "Too High", "Too Low"],
    attempt_number: int,
):
    if outcome not in {"Win", "Too High", "Too Low"}:
        raise ValueError(f"Invalid outcome: {outcome}")

    if outcome == "Win":
        points = 100 - 10 * attempt_number
        if points < 10:
            points = 10
        return current_score + points
    else:
        return current_score - 5
