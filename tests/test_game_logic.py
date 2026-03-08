import sys

sys.path.append("..")

from logic_utils import (
    check_guess,
    get_range_for_difficulty,
    parse_guess,
    update_score,
)


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == ("Win", "🎉 Correct!")


def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == ("Too High", "📉 Go LOWER!")


def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == ("Too Low", "📈 Go HIGHER!")


def test_update_score():
    # Winning on the first attempt should give 100 points
    score = update_score(current_score=0, outcome="Win", attempt_number=1)
    assert score == 100
    # Winning on the second attempt should give 90 points
    score = update_score(current_score=0, outcome="Win", attempt_number=2)
    assert score == 90
    # Winning on the tenth attempt should give 10 points
    score = update_score(current_score=0, outcome="Win", attempt_number=10)
    assert score == 10
    # Winning on the eleventh attempt should also give 10 points (minimum)
    score = update_score(current_score=0, outcome="Win", attempt_number=11)
    assert score == 10
    # Incorrect guess should deduct 5 points
    score = update_score(current_score=100, outcome="Too High", attempt_number=1)
    assert score == 95
    score = update_score(current_score=95, outcome="Too Low", attempt_number=2)
    assert score == 90


def test_get_range_for_difficulty():
    # Easy difficulty should return (1, 20)
    assert get_range_for_difficulty("Easy") == (1, 20)
    # Normal difficulty should return (1, 50)
    assert get_range_for_difficulty("Normal") == (1, 50)
    # Hard difficulty should return (1, 100)
    assert get_range_for_difficulty("Hard") == (1, 100)
    # Invalid difficulty should raise ValueError
    try:
        get_range_for_difficulty("Invalid")
        assert False, "Expected ValueError for invalid difficulty"
    except ValueError:
        pass


def test_parse_guess():
    # Valid integer guess
    ok, value, err = parse_guess("42", 1, 100)
    assert ok and value == 42 and err is None

    # Valid float guess that can be converted to int
    ok, value, err = parse_guess("42.0", 1, 100)
    assert ok and value == 42 and err is None

    # Empty input
    ok, value, err = parse_guess("", 1, 100)
    assert not ok and value is None and err == "Enter a guess."

    # Non-numeric input
    ok, value, err = parse_guess("abc", 1, 100)
    assert not ok and value is None and err == "That is not a number."

    # Guess below range
    ok, value, err = parse_guess("0", 1, 100)
    assert not ok and value is None and err == "Guess must be between 1 and 100."

    # Guess above range
    ok, value, err = parse_guess("101", 1, 100)
    assert not ok and value is None and err == "Guess must be between 1 and 100."
