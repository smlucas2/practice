"""
Game Logic Module

This module handles the core game mechanics including random number generation,
guess validation, and feedback calculation for the Hot-Cold number guessing game.
"""

import random
from typing import Tuple

class GameLogic:
    """
    Manages the game's core logic including number generation and guess evaluation.
    """
    
    def __init__(self):
        """Initialize game state with a random target number."""
        self.target_number = None
        self.previous_distance = None
        self.min_number = 1
        self.max_number = 100
        self.generate_number()

    def generate_number(self) -> None:
        """Generate a new random target number between min and max bounds."""
        self.target_number = random.randint(self.min_number, self.max_number)
        self.previous_distance = None

    def validate_guess(self, guess: str) -> Tuple[bool, str]:
        """
        Validate if the guess is a valid integer within the allowed range.
        
        Args:
            guess: The user's guess as a string
            
        Returns:
            Tuple of (is_valid: bool, error_message: str)
        """
        try:
            num = int(guess)
            if self.min_number <= num <= self.max_number:
                return True, ""
            return False, f"Guess must be between {self.min_number} and {self.max_number}"
        except ValueError:
            return False, "Please enter a valid number"

    def check_guess(self, guess: str) -> Tuple[str, bool]:
        """
        Evaluate the guess and provide feedback.
        
        Args:
            guess: The user's guess as a string
            
        Returns:
            Tuple of (feedback: str, is_winner: bool)
        """
        is_valid, error_msg = self.validate_guess(guess)
        if not is_valid:
            return error_msg, False

        num_guess = int(guess)
        if num_guess == self.target_number:
            return "WINNER", True

        current_distance = abs(num_guess - self.target_number)
        
        if self.previous_distance is None:
            self.previous_distance = current_distance
            return "Start guessing!", False
            
        if current_distance < self.previous_distance:
            feedback = "hot"
        else:
            feedback = "cold"
            
        self.previous_distance = current_distance
        return feedback, False

    def reset_game(self) -> None:
        """Reset the game state with a new target number."""
        self.generate_number()
