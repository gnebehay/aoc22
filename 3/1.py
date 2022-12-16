with open('input') as f:
    lines = f.readlines()

total_sum = 0

for line in lines:
    line = line.strip()
    length = len(line)
    assert(length % 2 == 0)
    compartment1 = set(line[:length//2])
    compartment2 = set(line[length//2:])

    intersection = compartment1 & compartment2

    print(line)

    for item in intersection:
        ascii_value = ord(item)
        if ascii_value >= 97:
            priority = ascii_value - 96
        else:
            priority = ascii_value - 65 + 27

        print(f'{item}: {priority}')

        total_sum += priority

    print()

print(total_sum)
