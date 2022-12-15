fileName = 'puzzle.txt'


def find_outcome(outcomes, opp, mine, me, opponent):
    scores = [outcomes[(opp, x)] for x in me]
    if mine == 'X':
        return min(scores)
    elif mine == 'Z':
        return max(scores)
    else:
        return opponent[opp] + 3


opponent = {'A': 1, 'B': 2, 'C': 3}
me = {'X': 1, 'Y': 2, 'Z': 3}

outcomes = dict()
for opp in opponent:
    for mine in me:
        if me[mine] == opponent[opp]:
            outcomes[(opp, mine)] = me[mine] + 3
        elif (me[mine] + 1 - opponent[opp]) % 3 == 0:
            outcomes[(opp, mine)] = me[mine]
        else:
            outcomes[(opp, mine)] = me[mine] + 6

total = 0
total2 = 0
with open(fileName) as file:
    while(line := file.readline()):
        opp = line[0]
        mine = line[2]
        total += outcomes[(opp, mine)]
        total2 += find_outcome(outcomes, opp, mine, me, opponent)
print('part 1:', total)
print('part 2:', total2)
