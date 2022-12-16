file_name = 'puzzle.txt'
with open(file_name) as file:
    line = file.readline()
    for i in range(3, len(line)):
        if(len(set(line[i-4:i])) == 4):
            print('part 1', i)
            break
    for i in range(i, len(line)):
        if(len(set(line[i-14:i])) == 14):
            print('part 2', i)
            break
