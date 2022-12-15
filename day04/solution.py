from functools import cmp_to_key
fileName = 'puzzle.txt'
counter = 0
counter2 = 0


def compare_tuples(a, b):
    if a[0] == b[0]:
        return b[1] - a[1]
    else:
        return a[0] - b[0]


with open(fileName) as file:
    while(line := file.readline()):
        pairs = list(map(lambda x: tuple(map(int, x)), map(
            lambda x: x.split('-'), line.split(','))))
        pairs.sort(key=cmp_to_key(compare_tuples))
        if pairs[0][0] <= pairs[1][0] and pairs[0][1] >= pairs[1][1]:
            counter += 1
        if (pairs[0][0] <= pairs[1][0] and pairs[0][1] >= pairs[1][0]) or (pairs[0][1] >= pairs[1][1] and pairs[0][0] <= pairs[1][1]):
            counter2 += 1

print('part 1:', counter)
print('part 2:', counter2)
