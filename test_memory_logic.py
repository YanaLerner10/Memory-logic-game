import unittest
from memory_logic import MemoryGame, MemoryError

class TestMemoryGame(unittest.TestCase):
    def test_initialization(self):
        """Test that game starts with empty sequence and round 0."""
        game = MemoryGame()
        self.assertEqual(game.round, 0)
        self.assertEqual(game.sequence, [])
        self.assertFalse(game.over)

    def test_deterministic_seed(self):
        """Test that a seed produces the same sequence every time."""
        seed = 42
        game1 = MemoryGame(seed=seed)
        game2 = MemoryGame(seed=seed)
        
        seq1 = game1.next_round()
        seq2 = game2.next_round()
        
        self.assertEqual(seq1, seq2)
        # Ensure it works for multiple rounds
        self.assertEqual(game1.next_round(), game2.next_round())

    def test_game_flow_correct(self):
        """Test a standard game flow with correct answers."""
        # Fix the seed so we know the random numbers
        # With seed 1, Python's random might generate specific numbers. 
        # But we don't need to predict the numbers, just ensure check_response works.
        game = MemoryGame(seed=1) 
        
        # Round 1
        seq = game.next_round()
        correct, score = game.check_response(seq)
        self.assertTrue(correct)
        self.assertEqual(score, 1)
        self.assertFalse(game.over)

        # Round 2
        seq = game.next_round() # Sequence grows
        self.assertEqual(len(seq), 2)
        correct, score = game.check_response(seq)
        self.assertTrue(correct)
        self.assertEqual(score, 2)

    def test_game_over_incorrect(self):
        """Test that wrong answer ends game and calculates score correctly."""
        game = MemoryGame()
        
        # Round 1 - Success
        seq = game.next_round()
        game.check_response(seq) # Score is 1
        
        # Round 2 - Fail
        real_seq = game.next_round()
        
        # Create a wrong answer (append a wrong digit or change one)
        wrong_answer = real_seq.copy()
        wrong_answer[0] = (wrong_answer[0] + 1) % 10 
        
        correct, score = game.check_response(wrong_answer)
        
        self.assertFalse(correct)
        self.assertTrue(game.over)
        # Score should be 1 (completed round 1 successfully, failed round 2)
        self.assertEqual(score, 1)

    def test_cannot_play_after_game_over(self):
        """Ensure exceptions are raised if playing after game over."""
        game = MemoryGame()
        game.over = True
        
        with self.assertRaises(MemoryError):
            game.next_round()
            
        with self.assertRaises(MemoryError):
            game.check_response([1])

if __name__ == '__main__':
    unittest.main()