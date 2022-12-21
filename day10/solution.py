file_name = 'puzzle.txt'


def cycle_forward(cycle, x, buffer, signal_strengths):
    if((cycle % 40)-1 <= x + 1 and (cycle % 40)-1 >= x - 1):
        buffer.append('#')
    else:
        buffer.append('.')
    if (cycle + 20) % 40 == 0:
        signal_strengths.append(cycle * x)
    if cycle % 40 == 0:
        lines.append(buffer)
        buffer = []
    cycle += 1
    return cycle, buffer


with open(file_name) as file:
    cycle = 1
    x = 1
    signal_strengths = []
    buffer = []
    lines = []
    while line := file.readline().strip():
        if line.startswith('addx'):
            for _ in range(2):
                cycle, buffer = cycle_forward(
                    cycle, x, buffer, signal_strengths)
            x += int(line.split(' ')[1])
        else:
            cycle, buffer = cycle_forward(
                cycle, x, buffer, signal_strengths)

print('part 1:', sum(signal_strengths))
print('part 2:')
for line in lines:
    print(''.join(line))
