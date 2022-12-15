from functools import cmp_to_key
fileName = 'puzzle.txt'
counter = 0
counter2 = 0

with open(fileName) as file:
    while(line := file.readline()):
        pairs = list(map(lambda x: tuple(map(int, x)), map(
            lambda x: x.split('-'), line.split(','))))
        pairs.sort(key=cmp_to_key(
            lambda a, b: b[1] - a[1] if a[0] == b[0] else a[0] - b[0]))
        if pairs[0][0] <= pairs[1][0] and pairs[0][1] >= pairs[1][1]:
            counter += 1
        if (pairs[0][0] <= pairs[1][0] and pairs[0][1] >= pairs[1][0]) or (pairs[0][1] >= pairs[1][1] and pairs[0][0] <= pairs[1][1]):
            counter2 += 1

print('part 1:', counter)
print('part 2:', counter2)
