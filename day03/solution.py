fileName = 'puzzle.txt'


def get_score(char):
    score = ord(char)
    if score > 96:
        score -= ord('a') - 1
    else:
        score -= ord('A') - 27
    return score


with open(fileName) as file:
    lines = file.readlines()

total = 0
total2 = 0
for idx, line in enumerate(lines):
    first = set(line[:len(line)//2])
    second = set(line[len(line)//2:])
    intersection = first.intersection(second)
    for char in intersection:
        total += get_score(char)
    if idx % 3 == 0:
        sets = [set(line.strip()) for line in lines[idx:idx + 3]]
        intersection = sets[0].intersection(sets[1]).intersection(sets[2])
        for char in intersection:
            total2 += get_score(char)


print('part 1:', total)
print('part 2:', total2)
