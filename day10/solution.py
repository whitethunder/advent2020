import pathlib


with open(pathlib.Path(__file__).parent / 'input.txt') as file:
    adapters = sorted([int(x) for x in file])

# Add in outlet joltage of 0 and my device of max_adapter + 3
adapters.insert(0, 0)
adapters.append(adapters[-1] + 3)
counts = {1: 0, 3: 0}

for index in range(0, len(adapters) - 1):
    diff = adapters[index + 1] - adapters[index]
    counts[diff] += 1

print(counts[1] * counts[3])
# 2048

adapters.pop(0)
options = {}
options[0] = 1
for a in adapters:
    options[a] = options.get(a - 1, 0) + options.get(a - 2, 0) + options.get(a - 3, 0)

print(options[max(adapters)])
# 1322306994176
