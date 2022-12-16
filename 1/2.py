with open('input.txt') as f:

    groups = []

    current_group = []

    for line in f:

        line = line.strip()

        if line:
            current_group.append(int(line))
        else:
            groups.append(current_group)
            current_group = []

    groups.append(current_group)

    sums = sorted([sum(group) for group in groups], reverse=True)

    print(sum(sums[:3]))
