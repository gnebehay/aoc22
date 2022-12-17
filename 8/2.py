with open('input') as f:
    lines = f.read().splitlines()

result = [[1]*99 for _ in range(99)]

for _ in range(4):

    for i, line in enumerate(lines):

        for j, c in enumerate(line):

            current_height = int(c)

            for k in range(j+1, 99):

                if current_height <= int(line[k]):
                    result[i][j] *= k-j
                    break
            else:
                result[i][j] *= 98-j


    # Rotate input and result 90 degrees clockwise
    lines = list([list(el) for el in zip(*lines[::-1])])
    result = list([list(el) for el in zip(*result[::-1])])

print(max(max(line) for line in result))
