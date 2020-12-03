import re

valid_count = 0

# for line in open('valid.txt'):
for line in open('day2input.txt'):
    matches = re.search(r'(\d+)-(\d+)\s+(\w):\s(\w+)', line)
    min_count = int(matches.group(1))
    max_count = int(matches.group(2))
    char = matches.group(3)
    password = matches.group(4)

    charcount = password.count(char)

    if min_count <= charcount <= max_count:
        valid_count += 1

print(valid_count)

valid_count = 0
for line in open('day2input.txt'):
    matches = re.search(r'(\d+)-(\d+)\s+(\w):\s(\w+)', line)
    pos1 = int(matches.group(1)) - 1
    pos2 = int(matches.group(2)) - 1
    char = matches.group(3)
    password = matches.group(4)

    if (password[pos1] == char) ^ (password[pos2] == char):
        valid_count += 1

print(valid_count)
