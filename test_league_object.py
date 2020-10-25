import unittest
import subprocess
import unittest.mock
import io
import os

import league_object


class TestProcessResult(unittest.TestCase):
    """Test that single-line matches have the scores processed correctly
    
    These tests simultaniously tests the update_team method as the two methods
    are very closely coupled."""

    def test_given_input(self):
        """Test the input given in the brief"""

        league = league_object.League()

        league.process_result("Lions 3, Snakes 3")
        self.assertEqual(league.standings, [
                         {"team": "Lions", "points": 1},
                         {"team": "Snakes", "points": 1}])

        league.process_result("Tarantulas 1, FC Awesome 0")
        self.assertEqual(league.standings, [
                         {'team': 'Tarantulas', 'points': 3},
                         {'team': 'Lions', 'points': 1},
                         {'team': 'Snakes', 'points': 1},
                         {'team': 'FC Awesome', 'points': 0}])

        league.process_result("Lions 1, FC Awesome 1")
        self.assertEqual(league.standings, [
                         {'team': 'Tarantulas', 'points': 3},
                         {'team': 'Lions', 'points': 2},
                         {'team': 'FC Awesome', 'points': 1},
                         {'team': 'Snakes', 'points': 1}])

        league.process_result("Tarantulas 3, Snakes 1")
        self.assertEqual(league.standings, [
                         {'team': 'Tarantulas', 'points': 6},
                         {'team': 'Lions', 'points': 2},
                         {'team': 'FC Awesome', 'points': 1},
                         {'team': 'Snakes', 'points': 1}])

        league.process_result("Lions 4, Grouches 0")
        self.assertEqual(league.standings, [
                         {'team': 'Tarantulas', 'points': 6},
                         {'team': 'Lions', 'points': 5},
                         {'team': 'FC Awesome', 'points': 1},
                         {'team': 'Snakes', 'points': 1},
                         {'team': 'Grouches', 'points': 0}])

    def test_process_special_characters(self):
        league = league_object.League()

        # reset the standings for this test
        league.standings.clear()

        league.process_result("My $p3cial T34M 1, Y0uR C**L T3AM 3")
        self.assertEqual(league.standings, [
                         {"team": "Y0uR C**L T3AM", "points": 3},
                         {"team": "My $p3cial T34M", "points": 0}])

    def test_process_multi_didget_scores(self):
        league = league_object.League()
        league.standings.clear()

        league.process_result("Lions 42, Snakes 999")
        self.assertEqual(league.standings, [
            {"team": "Snakes", "points": 3},
            {"team": "Lions", "points": 0}, ])

    def test_process_team1_win(self):
        league = league_object.League()
        league.standings.clear()

        league.process_result("Team1 1, Team2 0")
        self.assertEqual(league.standings[0]["team"], "Team1")
        self.assertEqual(league.standings[0]["points"], 3)
        self.assertEqual(league.standings[1]["team"], "Team2")
        self.assertEqual(league.standings[1]["points"], 0)

    def test_process_team2_win(self):
        league = league_object.League()
        league.standings.clear()

        league.process_result("Team1 1, Team2 2")
        self.assertEqual(league.standings[0]["team"], "Team2")
        self.assertEqual(league.standings[0]["points"], 3)
        self.assertEqual(league.standings[1]["team"], "Team1")
        self.assertEqual(league.standings[1]["points"], 0)

    def test_process_draw(self):
        league = league_object.League()
        league.standings.clear()

        league.process_result("Team1 0, Team2 0")
        self.assertEqual(league.standings[0]["team"], "Team1")
        self.assertEqual(league.standings[0]["points"], 1)
        self.assertEqual(league.standings[1]["team"], "Team2")
        self.assertEqual(league.standings[1]["points"], 1)

class TestPrintStandings(unittest.TestCase):
    """Test that the League __str()__ metod works as inteded"""

    def test_print_example_data(self):
        league = league_object.League()
        league.standings = [{'team': 'Tarantulas', 'points': 6},
                         {'team': 'Lions', 'points': 5},
                         {'team': 'FC Awesome', 'points': 1},
                         {'team': 'Snakes', 'points': 1},
                         {'team': 'Grouches', 'points': 0}]

        expected = "1. Tarantulas, 6 pts" + os.linesep + \
            "2. Lions, 5 pts" + os.linesep + \
            "3. FC Awesome, 1 pt" + os.linesep + \
            "3. Snakes, 1 pt" + os.linesep + \
            "5. Grouches, 0 pts"

        self.assertEqual(str(league), expected)

    def test_print_one_pt(self):
        league = league_object.League()
        league.standings = [{"team": "FC Awesome", "points": 1}]

        expected = "1. FC Awesome, 1 pt"

        self.assertEqual(str(league), expected)

    def test_print_zero_pts(self):
        league = league_object.League()
        league.standings = [{"team": "FC Awesome", "points": 0}]

        expected = "1. FC Awesome, 0 pts"

        self.assertEqual(str(league), expected)

    def test_print_many_pnts(self):
        league = league_object.League()
        league.standings = [{"team": "Tarantulas", "points": 56}, 
                            {"team": "Lions", "points": 5}, 
                            {"team": "FC Awesome", "points": 2}]

        expected = "1. Tarantulas, 56 pts" + os.linesep + \
            "2. Lions, 5 pts" + os.linesep + "3. FC Awesome, 2 pts"

        self.assertEqual(str(league), expected)


if __name__ == "__main__":

    unittest.main()
