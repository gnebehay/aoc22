with open('input') as f:
    lines = f.read().splitlines()

groups = [lines[i:i + 3] for i in range(0, len(lines), 3)]

total_sum = 0

for group in groups:
    group_set = [set(line) for line in group]
    badge = set.intersection(*group_set)

    assert(len(badge) == 1)
    item = next(iter(badge))

    ascii_value = ord(item)
    if ascii_value >= 97:
        priority = ascii_value - 96
    else:
        priority = ascii_value - 65 + 27

    print(f'{item}: {priority}')

    total_sum += priority

print(total_sum)
