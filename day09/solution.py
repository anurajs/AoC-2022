file_name = 'puzzle.txt'
directions = {'R': (1, 0), 'U': (0, 1), 'L': (-1, 0), 'D': (0, -1)}
touching_points = {(1, 0), (1, 1), (0, 1), (-1, 1),
                   (-1, 0), (-1, -1), (0, -1), (1, -1), (0, 0)}


def add_coordinates(a, b):
    return (a[0] + b[0], a[1] + b[1])


def tying_the_knot(part1):
    visited = set()
    with open(file_name) as file:
        knots = [(0, 0) for _ in range(2 if part1 else 10)]
        while(line := file.readline()):
            direction, amount = line.split(' ')
            amount = int(amount)
            for _ in range(amount):
                knots[0] = add_coordinates(knots[0], directions[direction])
                next_knot = knots[0]
                for idx in range(1, len(knots)):
                    touching = False
                    knot = knots[idx]
                    for point in touching_points:
                        if next_knot == add_coordinates(knot, point):
                            touching = True
                            break
                    if not touching:
                        addition = (1 if next_knot[0] > knot[0] else 0 if next_knot[0] == knot[0] else -1,
                                    1 if next_knot[1] > knot[1] else 0 if next_knot[1] == knot[1] else -1
                                    )
                        knots[idx] = add_coordinates(knot, addition)
                    if(idx == (1 if part1 else 9)):
                        visited.add(knots[idx])
                    next_knot = knots[idx]
    return visited


print('part 1:', len(tying_the_knot(True)))
print('part 2:', len(tying_the_knot(False)))
