import re

class Bag:
    def __init__(self, raw_rules: str):
        self.rules = []

        if raw_rules != 'no other bags.':
            for rule in re.split(r' bags?[,.]\s*', raw_rules)[:-1]:
                result = re.match(r'(\d+) (.+)', rule)
                self.rules.append((int(result.group(1)), result.group(2)))


def dfs_part_1(graph: dict, bag_color: str, current_color: str, result: int) -> int:
    for _rule_count, rule_color in graph[current_color].rules:
        if rule_color == bag_color:
            result = 1
        else:
            result = dfs_part_1(graph, bag_color, rule_color, result)

    return result


def dfs_part_2(bag_color: str, rule_index: dict) -> int:
    return sum(
        count + count * dfs_part_2(color, rule_index)
        for count, color in rule_index[bag_color].rules
    )

filename = 'input.txt'
with open(filename) as file:
    rule_index = {}
    for line in file:
        color, raw_rules = line.split(' bags contain ')
        rule_index[color] = Bag(raw_rules.strip())

    bag_color = 'shiny gold'
    count = 0

    for current_color in rule_index.keys():
        count += dfs_part_1(rule_index, bag_color, current_color, 0)

    print(count)

    print(dfs_part_2(bag_color, rule_index))


# 254
# 6006
