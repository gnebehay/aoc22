# First version
with open('input') as f:
    lines = f.read().splitlines()

lr = []
for i, line in enumerate(lines):
    row = []

    max_height = -1

    for c in line:

        current_height = int(c)
        if current_height > max_height:
            row.append(True)
            max_height = current_height
        else:
            row.append(False)

    lr.append(row)


rl = []
for i, line in enumerate(lines):

    row = []

    max_height = -1

    for j in range(len(line)):

        current_height = int(line[98-j])
        if current_height > max_height:
            row.append(True)
            max_height = current_height
        else:
            row.append(False)

    row.reverse()

    rl.append(row)


tb = [[] for _ in range(99)]
for j in range(99):

    max_height = -1

    for i, line in enumerate(lines):

        current_height = int(line[j])
        if current_height > max_height:
            tb[i].append(True)
            max_height = current_height
        else:
            tb[i].append(False)

bt = [[] for _ in range(99)]
for j in range(99):

    max_height = -1

    for i in range(len(lines)):

        line = lines[98-i]

        current_height = int(line[j])
        if current_height > max_height:
            bt[98-i].append(True)
            max_height = current_height
        else:
            bt[98-i].append(False)

total_sum = 0

for i in range(99):
    for j in range(99):
        if lr[i][j] or rl[i][j] or tb[i][j] or bt[i][j]:
            total_sum += 1

print(total_sum)


# Second version, using the fact that the input is a square matrix, so it can be rotated

with open('input') as f:
    lines = f.read().splitlines()

result = [[False]*99 for _ in range(99)]

for _ in range(4):

    for i, line in enumerate(lines):

        max_height = -1

        for j, c in enumerate(line):

            current_height = int(c)
            if current_height > max_height:
                result[i][j] = True
                max_height = current_height


    # Rotate input and result 90 degrees clockwise
    lines = list([list(el) for el in zip(*lines[::-1])])
    result = list([list(el) for el in zip(*result[::-1])])

print(sum(sum(line) for line in result))
