"""
A simple CLI application which calculates the ranking table of a soccer league
given the results of every match.

This is my preferred implimentation. This problem does not warrent going for an
OO style of code.

I am implimenting an OO approach, to show my proficiency. See league_object.py

Author: Jayan Smart <jayandrinsmart@gmail.com>
"""

import os

POINTS_WON = 3
POINTS_DRAW = 1


def process_result(result, standings):
    """Process a singe match result and update the global standings accordingly.
    3 points for a win, 0 for a loss and 1 point to each team for a draw.

    Args:
        result (String): Single match result using the format: 
        [Team 1] [Score], [Team 2] [Score]
    """
    result = result.split(', ')
    team1 = " ".join(result[0].split()[:-1])
    team2 = " ".join(result[1].split()[:-1])
    team1_score = result[0].split()[-1]
    team2_score = result[1].split()[-1]

    if team1 not in standings:
        standings[team1] = 0

    if team2 not in standings:
        standings[team2] = 0

    # Team 1 wins, so no points for team 2
    if team1_score > team2_score:
        standings[team1] += POINTS_WON
    # Team 2 wins, so no points for team 1
    elif team2_score > team1_score:
        standings[team2] += POINTS_WON
    # Draw, so 1 point for each team
    else:
        standings[team1] += POINTS_DRAW
        standings[team2] += POINTS_DRAW

    return standings


def sort_standings(standings):
    """Sorts the standings from the team with the most points
    to the team with the least points. Ties are sorted alphabetically.

    Args:
        standings (Dict): A dictionary of each team and its assossiated
        score in the league.

    Returns:
        Dict: A dictionary with sorted keys.
    """

    # Runs the sorted function using a custom sort key:
    # The key first sorts the scores in ascending order, but as negatives
    # (effectively decending order). As a tie breaker the items are sorted in
    # alphabetical order.
    return dict(sorted(standings.items(), key=lambda x: (-x[1], x[0].lower())))


def format_standings_string(standings):
    """Formats the sorted summary into a string with the following format:
    1. Team1 4 pnts
    2. Team2 2 pnts
    2. Team3 2 pnts
    4. Team4 1 pt


    Args:
        standings (Dict): A sorted dictionary of team names and points
    """

    out = ""
    position = 0
    delta = 1
    current_score = None
    for team in standings:
        # Check if we should increment position or not
        if current_score is None or standings[team] < current_score:
            position += delta
            delta = 1
            current_score = standings[team]
        else:
            delta += 1

        if standings[team] == 1:
            out += "{}. {}, {} pt".format(position,
                                          team, standings[team]) + os.linesep
        else:
            out += "{}. {}, {} pts".format(position,
                                           team, standings[team]) + os.linesep
    return out.strip()


def main():
    standings = {}

    line = input(
        "Enter match results, one game per line. An empty line denotes completion:\n")

    while(line != ""):
        standings = process_result(line, standings)
        line = input()
    standings = sort_standings(standings)
    print(format_standings_string(standings))


if __name__ == "__main__":
    main()
