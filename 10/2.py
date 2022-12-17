with open('input') as f:
    lines = f.read().splitlines()

values = [1]

for line in lines:

    parts = line.split(' ')

    values.append(values[-1])

    if len(parts) == 2:
        values.append(values[-1] + int(parts[1]))

for j in range(6):
    for i in range(40):

        sprite_position  = values[j*40+i]

        if abs(sprite_position - i) <= 1:
            print('#', end='')
        else:
            print(' ', end='')
    print()
