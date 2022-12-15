import re

file_name = 'puzzle.txt'

regex = r"\[([A-Z])\]"
instruction_regex = r"move (\d+) from (\d+) to (\d+)"
stacks = [[] for _ in range(10)]
stacks2 = [[] for _ in range(10)]
matcher = re.compile(regex)
with open(file_name) as file:
    while line := file.readline():
        matches = list(matcher.finditer(line))
        if matches:
            for match in matches:
                stack_index = match.start() // 4
                stacks[stack_index] = [match.group(1), *stacks[stack_index]]
                stacks2[stack_index] = [match.group(1), *stacks[stack_index]]
        else:
            break
    file.readline()
    matcher = re.compile(instruction_regex)
    while line := file.readline().strip():
        m = matcher.match(line)
        amount, origin, to = [int(m.group(i)) for i in range(1, 4)]
        stacks[to - 1] = [*stacks[to - 1],
                          *reversed(stacks[origin - 1][-amount:])]
        stacks[origin - 1] = stacks[origin - 1][:-amount]
        stacks2[to - 1] = [*stacks2[to - 1], *stacks2[origin - 1][-amount:]]
        stacks2[origin - 1] = stacks2[origin - 1][:-amount]


result = [stack[-1] if stack else '' for stack in stacks]
result2 = [stack[-1] if stack else '' for stack in stacks2]

print('part 1:', ''.join(result))
print('part 2:', ''.join(result2))
