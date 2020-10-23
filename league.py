

points = {}


def process_result(result):
    result = result.split(', ')
    team1 = " ".join(result[0].split()[:-1])
    team2 = " ".join(result[1].split()[:-1])
    team1_score = result[0].split()[-1]
    team2_score = result[1].split()[-1]

    if not team1 in points:
        points[team1] = 0
    
    if not team2 in points:
        points[team2] = 0

    if team1_score > team2_score:
        points[team1] += 3

    elif team2_score > team1_score:
        points[team2] += 3
    
    else:
        # We know this is a draw
        points[team1] += 1
        points[team2] += 1

def print_standings():
    for i in points:
        print(i[0], i[1])

if __name__ == "__main__":
    
    line = input("Enter match results, one game per line. An empty line denotes completion:\n")

    while(line != ""):
        process_result(line)
        line = input()

    # This is not something I am super happy with, as we need to sort the list twice.
    # First alphabetically, then by decending score. The reason this works is that the 
    # sorted() function maintains original order in the event of ties. 
    # 
    # I would prefer a solution like: 
    # points  = sorted(points.items(), key=lambda x: (x[1], x[0].lower()), reverse=True)
    # 
    # But the revese=True here is needed for the score but then breaks the alphabetical tie break. 
    alpha = sorted(points.items(), key=lambda x: x[0].lower(), reverse=False)
    points  = sorted(alpha, key=lambda x: x[1], reverse=True)

    print_standings()


"""
Lions 3, Snakes 3
Tarantulas 1, FC Awesome 0
Lions 1, FC Awesome 1
Tarantulas 3, Snakes 1
Lions 4, Grouches 0
My Awesome Team FC 20, Tarantulas 99
q 1, w 1
f 1, t 1
d 1, e 1
z 1, x 1
y 1, v 1
AAA 1, aaa 1
bbb 1, BBB 1
"""