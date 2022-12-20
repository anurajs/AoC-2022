file_name = 'puzzle.txt'
with open(file_name) as file:
    trees = []
    while(line := file.readline().strip()):
        row = []
        for char in line:
            row.append(int(char))
        trees.append(row)
    visible_trees = set()
    for i in range(len(trees)):
        prev = -1
        for j in range(len(trees[0])):
            if trees[i][j] > prev:
                visible_trees.add((i, j))
                prev = trees[i][j]
        prev = -1
        for j in range(len(trees[0])-1, -1, -1):
            if trees[i][j] > prev:
                visible_trees.add((i, j))
                prev = trees[i][j]
    for j in range(len(trees[0])):
        prev = -1
        for i in range(len(trees)):
            if trees[i][j] > prev:
                visible_trees.add((i, j))
                prev = trees[i][j]
        prev = -1
        for i in range(len(trees)-1, -1, -1):
            if trees[i][j] > prev:
                visible_trees.add((i, j))
                prev = trees[i][j]
    max_score = 0
    for i in range(len(trees)):
        for j in range(len(trees[0])):
            score = 1
            num_trees = 0
            for k in range(i+1, len(trees)):
                if trees[i][j] > trees[k][j]:
                    num_trees += 1
                else:
                    num_trees += 1
                    break
            score *= num_trees
            num_trees = 0
            for k in range(i-1, -1, -1):
                if trees[i][j] > trees[k][j]:
                    num_trees += 1
                else:
                    num_trees += 1
                    break
            score *= num_trees
            num_trees = 0
            for k in range(j+1, len(trees[0])):
                if trees[i][j] > trees[i][k]:
                    num_trees += 1
                else:
                    num_trees += 1
                    break
            score *= num_trees
            num_trees = 0
            for k in range(j-1, -1, -1):
                if trees[i][j] > trees[i][k]:
                    num_trees += 1
                else:
                    num_trees += 1
                    break
            score *= num_trees
            if score > max_score:
                max_score = score

print('part 1:', len(visible_trees))
print('part 2:', max_score)

# for i in range(len(trees)):
#     buffer = ''
#     for j in range(len(trees[0])):
#         if (i, j) in visible_trees:
#             buffer += str(trees[i][j])
#         else:
#             buffer += ' '

#     print(buffer)
