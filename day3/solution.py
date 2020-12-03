TREE = '#'

def count_trees(lines, steps):
    position = steps[0]
    line_num = steps[1]
    tree_count = 0

    while line_num < len(lines):
        if lines[line_num][position % (len(lines[line_num]))] == TREE:
            tree_count += 1

        position += steps[0]
        line_num += steps[1]

    return tree_count


file = open('input.txt')
lines = file.read().splitlines()

print("Part 1 Solution")
print(count_trees(lines, (3,1)))

print("Part 2 Solution")
result = 1
for t in [(1,1), (3,1), (5,1), (7,1), (1,2)]:
    result *= count_trees(lines, t)
print(result)
