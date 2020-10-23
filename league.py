"""
A simple CLI application which calculates the ranking table of a soccer league
given the results of every match.

Author: Jayan Smart <jayandrinsmart@gmail.com>
"""


def process_result(result, standings):
    """Process a singe match result and update the global standings accordingly.
    3 points for a win, 0 for a loss and 1 point to each team for a draw.

    Args:
        result (String): Single match result using the format: 
        <Team 1> <Score>, <Team 2> <Score>
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
        standings[team1] += 3
    # Team 2 wins, so no points for team 1
    elif team2_score > team1_score:
        standings[team2] += 3
    # Draw, so 1 point for each team
    else:
        standings[team1] += 1
        standings[team2] += 1

    return standings


def sort_standings(standings):
    """Sorts the standings from the team with the most points
    to the team with the least points. Ties are sorted alphabetically.

    Args:
        standings (Dict): A dictionary of eache team and their assossiated
        score in the league.

    Returns:
        List: A sorted list of Touples.
    """

    # Runs the sorted function using a custom sort key:
    # The key first sorts the scores in ascending order, but as negatives
    # (effectivly decending order). As a tie breaker the items are sorted in
    # alphabetical order.
    return sorted(standings.items(), key=lambda x: (-x[1], x[0].lower()))


def print_standings(standings):
    position = 0
    delta = 1
    current_score = None
    for team in standings:
        # Check if we should increment position or not
        if current_score is None or team[1] < current_score:
            position += delta
            delta = 1
            current_score = team[1]
        else:
            delta += 1

        if team[1] == 1:
            print("{}. {}, {} pt".format(position, team[0], team[1]))
        else:
            print("{}. {}, {} pts".format(position, team[0], team[1]))


def main():
    standings = {}

    line = input(
        "Enter match results, one game per line. An empty line denotes completion:\n")

    while(line != ""):
        standings = process_result(line, standings)
        line = input()
    standings = sort_standings(standings)
    print_standings(standings)


if __name__ == "__main__":
    main()
