with open("puzzle.txt") as file:
    elves = []
    food = 0
    while(len(line := file.readline()) != 0):
        line = line.strip()
        if len(line) == 0:
            elves.append(food)
            food = 0
            continue
        food += int(line)

elves.sort()
print(sum(elves[-3:]))
