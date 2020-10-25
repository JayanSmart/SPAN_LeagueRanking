from sortedcontainers import SortedKeyList, SortedDict


class League():

    standings = SortedKeyList(key=lambda x: (-x["points"], x["team"].lower()))
    POINTS_WON = 3
    POINTS_DRAW = 1
    POINTS_LOSS = 0

    def process_result(self, result):
        """Process a singe match result and update the standings accordingly.
        3 points for a win, 0 for a loss and 1 point to each team for a draw.

        Args:
            result (String): Single match result using the format: 
            [Team 1] [Score], [Team 2] [Score]
        """
        result = result.split(', ')
        team1 = " ".join(result[0].split()[:-1])
        team2 = " ".join(result[1].split()[:-1])
        team1_score = int(result[0].split()[-1])
        team2_score = int(result[1].split()[-1])

        # Team 1 wins, so no points for team 2
        if team1_score > team2_score:
            self.update_team(team1, self.POINTS_WON)
            self.update_team(team2, self.POINTS_LOSS)
        # Team 2 wins, so no points for team 1
        elif team2_score > team1_score:
            self.update_team(team1, self.POINTS_LOSS)
            self.update_team(team2, self.POINTS_WON)
        # Draw, so 1 point for each team
        else:
            self.update_team(team1, self.POINTS_DRAW)
            self.update_team(team2, self.POINTS_DRAW)

    def update_team(self, team, points):
        """Add a number of points to a particular team. 
        If the team does not exist, add the team.

        Args:
            team (String): The name of the team to update
            points (int): The number of points to add to the given team
        """
        for i in self.standings:
            if team == i["team"]:
                points += i["points"]
                self.standings.remove(i)
        self.standings.add({"team": team, "points": points})

    def __str__(self):
        """Formats the standings object into a printable string using the 
        following format:
            1. Team1 4 pnts
            2. Team2 2 pnts
            2. Team3 2 pnts
            4. Team4 1 pt

        Returns:
            String: A formatted string of the standings object.
        """
        out = ""

        position = 0
        delta = 1
        current_score = None
        for team in self.standings:
            # Check if we should increment position or not
            if current_score is None or team["points"] < current_score:
                position += delta
                delta = 1
                current_score = team["points"]
            else:
                delta += 1

            if team["points"] == 1:
                out += "{}. {}, {} pt\n".format(position,
                                                team["team"], team["points"])
            else:
                out += "{}. {}, {} pts\n".format(position,
                                                 team["team"], team["points"])
        return out.strip()


def main():
    league = League()

    line = input(
        "Enter match results, one game per line. An empty line denotes completion:\n")

    while(line != ""):
        league.process_result(line)
        line = input()

    print(league)


if __name__ == "__main__":
    main()
