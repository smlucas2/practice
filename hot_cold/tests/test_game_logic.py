"""
Test Game Logic Module

This module contains unit tests for the game logic of the Hot-Cold number guessing game.
"""

import unittest
from src.game_logic import GameLogic

class TestGameLogic(unittest.TestCase):
    """Test cases for the GameLogic class."""

    def setUp(self):
        """Set up test fixtures before each test method."""
        self.game = GameLogic()
        # Force a specific target number for testing
        self.game.target_number = 50

    def test_validate_guess_valid_number(self):
        """Test that valid numbers are accepted."""
        is_valid, error = self.game.validate_guess("50")
        self.assertTrue(is_valid)
        self.assertEqual(error, "")

    def test_validate_guess_invalid_input(self):
        """Test that non-numeric input is rejected."""
        is_valid, error = self.game.validate_guess("abc")
        self.assertFalse(is_valid)
        self.assertEqual(error, "Please enter a valid number")

    def test_validate_guess_out_of_range(self):
        """Test that numbers outside the valid range are rejected."""
        is_valid, error = self.game.validate_guess("101")
        self.assertFalse(is_valid)
        self.assertEqual(error, "Guess must be between 1 and 100")

    def test_check_guess_winner(self):
        """Test that correct guess is identified as winner."""
        feedback, is_winner = self.game.check_guess("50")
        self.assertTrue(is_winner)
        self.assertEqual(feedback, "WINNER")

    def test_check_guess_hot(self):
        """Test that closer guess returns 'hot'."""
        # First guess
        self.game.check_guess("20")
        # Second guess closer to target (50)
        feedback, is_winner = self.game.check_guess("40")
        self.assertFalse(is_winner)
        self.assertEqual(feedback, "hot")

    def test_check_guess_cold(self):
        """Test that farther guess returns 'cold'."""
        # First guess
        self.game.check_guess("40")
        # Second guess farther from target (50)
        feedback, is_winner = self.game.check_guess("20")
        self.assertFalse(is_winner)
        self.assertEqual(feedback, "cold")

    def test_reset_game(self):
        """Test that game reset generates new number and resets state."""
        old_target = self.game.target_number
        self.game.previous_distance = 10
        
        self.game.reset_game()
        
        self.assertIsNone(self.game.previous_distance)
        # Note: There's a small chance this could fail if the new random
        # number happens to be the same as the old one
        self.assertNotEqual(old_target, self.game.target_number)

if __name__ == '__main__':
    unittest.main()
