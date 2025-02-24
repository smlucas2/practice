import unittest
from src.game_logic import GameLogic

class TestGameLogic(unittest.TestCase):

    def setUp(self):
        self.game = GameLogic()
        self.game.target_number = 50

    def test_validate_guess_valid_number(self):
        is_valid, error = self.game.validate_guess("50")
        self.assertTrue(is_valid)
        self.assertEqual(error, "")

    def test_validate_guess_invalid_input(self):
        is_valid, error = self.game.validate_guess("abc")
        self.assertFalse(is_valid)
        self.assertEqual(error, "Guess must be between 1 and 100")

    def test_validate_guess_out_of_range(self):
        is_valid, error = self.game.validate_guess("101")
        self.assertFalse(is_valid)
        self.assertEqual(error, "Guess must be between 1 and 100")

    def test_validate_guess_lower_bound(self):
        is_valid, error = self.game.validate_guess("1")
        self.assertTrue(is_valid)
        self.assertEqual(error, "")

    def test_validate_guess_upper_bound(self):
        is_valid, error = self.game.validate_guess("100")
        self.assertTrue(is_valid)
        self.assertEqual(error, "")

    def test_validate_guess_negative_number(self):
        is_valid, error = self.game.validate_guess("-5")
        self.assertFalse(is_valid)
        self.assertEqual(error, "Guess must be between 1 and 100")

    def test_check_guess_winner(self):
        feedback, is_winner = self.game.check_guess("50")
        self.assertTrue(is_winner)
        self.assertEqual(feedback, "WINNER")

    def test_check_guess_hot(self):
        self.game.check_guess("20")
        feedback, is_winner = self.game.check_guess("40")
        self.assertFalse(is_winner)
        self.assertEqual(feedback, self.game.HOT)

    def test_check_guess_cold(self):
        self.game.check_guess("40")
        feedback, is_winner = self.game.check_guess("20")
        self.assertFalse(is_winner)
        self.assertEqual(feedback, self.game.COLD)

    def test_check_guess_first_guess(self):
        feedback, is_winner = self.game.check_guess("30")
        self.assertFalse(is_winner)
        self.assertEqual(feedback, "Now guess closer!")

    def test_check_guess_invalid_guess(self):
        feedback, is_winner = self.game.check_guess("abc")
        self.assertFalse(is_winner)
        self.assertEqual(feedback, "Guess must be between 1 and 100")

    def test_check_guess_out_of_range(self):
        feedback, is_winner = self.game.check_guess("101")
        self.assertFalse(is_winner)
        self.assertEqual(feedback, "Guess must be between 1 and 100")

    def test_reset_game(self):
        max_retries = 100
        retries = 0
        # 1:100 chance that the same number is generated again, so we retry a few times
        while retries < max_retries:
            old_target = self.game.target_number
            self.game.previous_distance = 10
            self.game.reset_game()
            if self.game.target_number != old_target:
                self.assertIsNone(self.game.previous_distance)
                self.assertNotEqual(old_target, self.game.target_number)
                break
            retries += 1

if __name__ == '__main__':
    unittest.main()