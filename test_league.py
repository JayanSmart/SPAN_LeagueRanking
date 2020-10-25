import unittest
import subprocess
import unittest.mock
import io

import league


class TestProcessResult(unittest.TestCase):
    """Test that single-line matches have the scores processed correctly"""

    def test_given_input(self):
        """Test the input given in the brief"""
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
        standings = {"Lions": 5, "Snakes": 1, "Tarantulas": 6, "FC Awesome": 1, "Grouches": 0}

        self.assertEqual(league.sort_standings(standings), {"Tarantulas": 6, "Lions": 5, "FC Awesome": 1, "Snakes": 1, "Grouches": 0})

    def test_sort_case_insensitive(self):
        standings = {"Apples": 5, "Pears": 1, "Bannana": 6, "peaches": 1, "graPes": 0}
        self.assertEqual(league.sort_standings(standings), {"Bannana": 6, "Apples": 5, "peaches": 1, "Pears": 1, "graPes": 0})

    def test_sort_number_in_name(self):
        standings = {"team1": 1, "team2": 1}
        self.assertEqual(league.sort_standings(standings), {"team1": 1, "team2": 1})

    def test_sort_symbol_in_name(self):
        standings = {"team@": 1, "team!": 1}
        self.assertEqual(league.sort_standings(standings), {"team!": 1, "team@": 1})

    def test_sort_score_then_alpha(self):
        standings = {"a": 0, "b": 1, "c": 3, "d": 1}
        self.assertEqual(league.sort_standings(standings), {"c": 3, "b": 1, "d": 1, "a": 0})


class TestPrintStandings(unittest.TestCase):
    """Test that the print_standings method works as intended

    Some IDE's will show an error at every call of 'self.assert_stdout()'.
    The code will run but the mocking annotation used to capture stdOut
    is not widely recognised by IDE's"""

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout(self, standings, expected_output, mock_stdout):
        league.print_standings(standings)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_print_example_data(self):
        standings = {"Tarantulas": 6, "Lions": 5, "FC Awesome": 1, "Snakes": 1, "Grouches": 0}

        expected = "1. Tarantulas, 6 pts\n2. Lions, 5 pts\n3. FC Awesome, 1 pt\n3. Snakes, 1 pt\n5. Grouches, 0 pts\n"

        self.assert_stdout(standings, expected)

    def test_print_one_pt(self):
        standings = {"FC Awesome": 1}

        expected = "1. FC Awesome, 1 pt\n"

        self.assert_stdout(standings, expected)

    def test_print_zero_pts(self):
        standings = {"FC Awesome": 0}

        expected = "1. FC Awesome, 0 pts\n"

        self.assert_stdout(standings, expected)

    def test_print_many_pnts(self):
        standings = {"Tarantulas": 56, "Lions": 5, "FC Awesome": 2}

        expected = "1. Tarantulas, 56 pts\n2. Lions, 5 pts\n3. FC Awesome, 2 pts\n"

        self.assert_stdout(standings, expected)


if __name__ == "__main__":
    unittest.main()
