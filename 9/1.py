with open('input') as f:
    lines = f.read().splitlines()

head = (0, 0)
tail = (0, 0)
seen_positions = set()
seen_positions.add(tail)

sign = lambda x: -1 if x < 0 else (1 if x > 0 else 0)

for line in lines:

    direction, steps = line.split(' ')

    for _ in range(int(steps)):

        if direction == 'U':
            head = (head[0], head[1]+1)
        if direction == 'R':
            head = (head[0]+1, head[1])
        if direction == 'D':
            head = (head[0], head[1]-1)
        if direction == 'L':
            head = (head[0]-1, head[1])

        dx = head[0] - tail[0]
        dy = head[1] - tail[1]

        if abs(dx) == 2 or abs(dy) == 2:
            tail = (tail[0] + sign(dx), tail[1] + sign(dy))
            seen_positions.add(tail)

print(len(seen_positions))
