import pathlib

with open(pathlib.Path(__file__).parent / 'input.txt') as file:
    file = file.read().split("\n\n")

    print(
        sum(
            len(set(group.replace('\n', ''))) for group in file
        )
    )

    sum = 0
    for group in file:
        group = group.split("\n")
        group_set = set(group[0])

        for answers in group[1:]:
            group_set = group_set.intersection(set(answers))

        sum += len(group_set)

    print(sum)

# 7110
# 3628
