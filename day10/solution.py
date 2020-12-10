import pathlib

with open(pathlib.Path(__file__).parent / 'input.txt') as file:
    adapters = file.read().splitlines()
    adapters = list(map(int, adapters))
    adapters.append(0)
    adapters.sort()
    adapters.append(adapters[-1] + 3)

one_count = 0
three_count = 1
for index in range(0, len(adapters) - 1):
    diff = adapters[index + 1] - adapters[index]
    if diff == 1:
        one_count += 1
    elif diff == 3:
        three_count += 1

print(one_count * three_count)
# 2048
