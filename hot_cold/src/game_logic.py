import random
from typing import Tuple

class GameLogic:
    HOT = "HOT"
    COLD = "COLD"

    def __init__(self):
        self.min_number = 1
        self.max_number = 100
        self.reset_game()

    def reset_game(self) -> None:
        """
        Resets the game by generating a new target number and resetting the previous distance.
        """
        self.target_number = self._generate_target_number()
        self.previous_distance = None

    def validate_guess(self, guess: str) -> Tuple[bool, str]:
        """
        Validates the user's guess to ensure it is within the acceptable range.

        Args:
            guess (str): The user's guess as a string.

        Returns:
            Tuple[bool, str]: A tuple where the first element is a boolean indicating if the guess is valid,
                             and the second element is an error message if the guess is invalid.
        """
        if not self._is_valid_number(guess):
            return False, f"Guess must be between {self.min_number} and {self.max_number}"
        return True, ""

    def check_guess(self, guess: str) -> Tuple[str, bool]:
        """
        Checks the user's guess against the target number and provides feedback.

        Args:
            guess (str): The user's guess as a string.

        Returns:
            Tuple[str, bool]: A tuple where the first element is a feedback message,
                             and the second element is a boolean indicating if the guess is correct.
        """
        is_valid, error_msg = self.validate_guess(guess)
        if not is_valid:
            return error_msg, False

        num_guess = int(guess)
        if num_guess == self.target_number:
            return "WINNER!", True

        current_distance = abs(num_guess - self.target_number)
        feedback = self._provide_feedback(current_distance)
        self.previous_distance = current_distance
        return feedback, False

    def _generate_target_number(self) -> int:
        return random.randint(self.min_number, self.max_number)

    def _is_valid_number(self, guess: str) -> bool:
        try:
            num = int(guess)
            return self.min_number <= num <= self.max_number
        except ValueError:
            return False

    def _provide_feedback(self, current_distance: int) -> str:
        if self.previous_distance is None:
            return "Now guess closer!"
        return self.HOT if current_distance < self.previous_distance else self.COLD
