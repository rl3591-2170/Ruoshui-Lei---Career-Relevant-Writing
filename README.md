README -  wordle_lei_ruoshui

1. Description  
This is a Python package I built. It’s basically a few helper functions that simulate how the game Wordle works. I created it to practice how to structure a project, document code, and publish it to TestPyPI. The functions are simple, but they cover the full cycle of building, testing, and packaging a Python project.

2. Functions 
1）、validate_guess: checks if a guess is valid (only lowercase letters, correct length)  
2）、check_guess: compares a guess with the secret word and returns color hints like green, yellow, or gray  
3）、is_valid_word: checks if a given word exists in a list of valid words  
4）、calculate_game_score: calculates a score based on how many guesses are used  

3. Example usage  
import wordle_lei_ruoshui as wl  
print(wl.validate_guess("crane"))  
print(wl.check_guess("react", "crate"))  
print(wl.calculate_game_score(guesses_used=4))

4. Tests and coverage  
I used pytest and pytest-cov to run the tests and measure coverage.  
To test everything, I ran this command:  
poetry run pytest --cov=wordle_lei_ruoshui --cov-report=term --cov-report=html  
Then I checked the htmlcov/index.html file for the detailed coverage report.  
A screenshot of that report is included in my homework notebook.

5. Links  
TestPyPI: https://test.pypi.org/project/wordle-lei-ruoshui/  
GitHub: https://github.com/your_github_username/wordle_lei_ruoshui  

6. License  
MIT License

7. Notes  
It was actually fun to see how everything fits together, even if it was just for a simple game like Wordle. It also helped me understand how tools like poetry, pytest, and PyPI work in real projects.
