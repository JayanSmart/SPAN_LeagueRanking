import unittest

import league

class TestLeageProcessing(unittest.TestCase):

    """
    Test that each line from the example is processed as expected
    """
    def test_given_input(self):

        # Ensure the dictionary is initalised empty
        league.points = {}

        league.process_result('Lions 3, Snakes 3')
        self.assertEqual(league.points, {'Lions': 1, 'Snakes': 1})

        league.process_result('Tarantulas 1, FC Awesome 0')
        self.assertEqual(league.points, {'Lions': 1, 'Snakes': 1, 'Tarantulas': 3, 'FC Awesome': 0})

        league.process_result('Lions 1, FC Awesome 1')
        self.assertEqual(league.points, {'Lions': 2, 'Snakes': 1, 'Tarantulas': 3, 'FC Awesome': 1})

        league.process_result('Tarantulas 3, Snakes 1')
        self.assertEqual(league.points, {'Lions': 2, 'Snakes': 1, 'Tarantulas': 6, 'FC Awesome': 1})

        league.process_result('Lions 4, Grouches 0')
        self.assertEqual(league.points, {'Lions': 5, 'Snakes': 1, 'Tarantulas': 6, 'FC Awesome': 1, 'Grouches': 0})

            
    def test_process_special_characters(self):
        league.points = {}

        league.process_result('My $p3cial T34M 1, Y0uR C**L T3AM 3')
        self.assertEqual(league.points, {'My $p3cial T34M': 0, 'Y0uR C**L T3AM': 3})

    def test_process_multi_didget_scores(self):
        # Ensure the dictionary is initalised empty
        league.points = {}

        league.process_result('Lions 42, Snakes 999')
        self.assertEqual(league.points, {'Lions': 0, 'Snakes': 3})


"""
Lions 3, Snakes 3
Tarantulas 1, FC Awesome 0
Lions 1, FC Awesome 1
Tarantulas 3, Snakes 1
Lions 4, Grouches 0
"""

if __name__ == "__main__":
    unittest.main()