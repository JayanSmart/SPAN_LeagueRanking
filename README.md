# League: A soccer rank calculator

---
**Note**

This application was written as a part of the SPAN Digital Innovation interview process. 
The given brief, "BE Coding Test - Candidate.pdf", is submitted to this repository.

---

This is a simple CLI application that will calculate the ranking table for a
soccer league, given the match results as input.

## Usage

``` bash
python league.py

Enter match results, one game per line. An empty line denotes completion:
Lions 3, Snakes 3
Tarantulas 1, FC Awesome 0
Lions 1, FC Awesome 1
Tarantulas 3, Snakes 1
Lions 4, Grouches 0

1. Tarantulas, 6 pts
2. Lions, 5 pts
3. FC Awesome, 1 pt
3. Snakes, 1 pt
5. Grouches, 0 pts

```

### Input

Using stdin, input one match result per line in the following format:

[Team 1] [Score], [Team 2] [Score]

### Output

Output will be formatted as in the above approach with each line following the following format:

[Position]. [Team Name] [Points] pt(s)

Note that teams with the same number of points, will receive the same postilion, and are sorted alphabetically.

## league_object.py

This is a second solution which was written as a demonstration of a more Object Oriented approach, though it does only make use of one additional class. This is my less preferred solution. Note that this solution also has a required package: sortedcontainers.

This package's usage is the same as league.py

## Requirements

Python 3.8 or newer

For league_object.py the package sortedcontainers is also required, 
the tested version can be found in requirements.txt

## License

[MIT](https://choosealicense.com/licenses/mit/)
