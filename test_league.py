import unittest

import league


class TestProcessResult(unittest.TestCase):
    """
    Test that single-line matches have the scores processed correctly
    """

    def test_given_input(self):
        """Test the input given in the brief
        """
        # Ensure the dictionary is initalised empty
        standings = {}

        standings = league.process_result("Lions 3, Snakes 3", standings)
        self.assertEqual(standings, {"Lions": 1, "Snakes": 1})

        standings = league.process_result(
            "Tarantulas 1, FC Awesome 0", standings)
        self.assertEqual(
            standings, {"Lions": 1, "Snakes": 1, "Tarantulas": 3, "FC Awesome": 0})

        standings = league.process_result("Lions 1, FC Awesome 1", standings)
        self.assertEqual(
            standings, {"Lions": 2, "Snakes": 1, "Tarantulas": 3, "FC Awesome": 1})

        standings = league.process_result("Tarantulas 3, Snakes 1", standings)
        self.assertEqual(
            standings, {"Lions": 2, "Snakes": 1, "Tarantulas": 6, "FC Awesome": 1})

        standings = league.process_result("Lions 4, Grouches 0", standings)
        self.assertEqual(standings, {
                         "Lions": 5, "Snakes": 1, "Tarantulas": 6, "FC Awesome": 1, "Grouches": 0})

    def test_process_special_characters(self):
        standings = {}
        standings = league.process_result(
            "My $p3cial T34M 1, Y0uR C**L T3AM 3", standings)
        self.assertEqual(
            standings, {"My $p3cial T34M": 0, "Y0uR C**L T3AM": 3})

    def test_process_multi_didget_scores(self):
        standings = {}

        standings = league.process_result("Lions 42, Snakes 999", standings)
        self.assertEqual(standings, {"Lions": 0, "Snakes": 3})

    def test_process_team1_win(self):
        standings = {}

        standings = league.process_result("Team1 1, Team2 0", standings)
        self.assertEqual(standings["Team1"], 3)
        self.assertEqual(standings["Team2"], 0)

    def test_process_team2_win(self):
        standings = {}

        standings = league.process_result("Team1 0, Team2 1", standings)
        self.assertEqual(standings["Team1"], 0)
        self.assertEqual(standings["Team2"], 3)

    def test_process_draw(self):
        standings = {}

        standings = league.process_result("Team1 1, Team2 1", standings)
        self.assertEqual(standings["Team1"], 1)
        self.assertEqual(standings["Team2"], 1)


class TestSortStandings(unittest.TestCase):
    """
    Test that the sorting of the standings is correct
    """

    def test_sort_example_data(self):
        standings = {"Lions": 5, "Snakes": 1,
                     "Tarantulas": 6, "FC Awesome": 1, "Grouches": 0}

        self.assertEqual(league.sort_standings(standings), [
                         ('Tarantulas', 6), ('Lions', 5), ('FC Awesome', 1), 
                         ('Snakes', 1), ('Grouches', 0)])



if __name__ == "__main__":
    unittest.main()
