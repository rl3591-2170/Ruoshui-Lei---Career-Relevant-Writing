from wordle_lei_ruoshui import validate_guess, check_guess, is_valid_word, calculate_game_score

def test_validate_guess():
    assert validate_guess("crane")
    assert not validate_guess("CRANE")
    assert not validate_guess("cat", 5)

def test_check_guess():
    res = check_guess("react", "crate")
    assert isinstance(res, list) and len(res) == 5

def test_is_valid_word():
    wl = ["crane", "apple", "hello"]
    assert is_valid_word("APPLE", wl)
    assert not is_valid_word("banana", wl)

def test_calculate_game_score():
    assert calculate_game_score(1) == 6
    assert calculate_game_score(6) == 1
    assert calculate_game_score(0) == 0
    assert calculate_game_score(7) == 0
