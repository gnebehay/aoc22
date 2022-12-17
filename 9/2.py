with open('input') as f:
    lines = f.read().splitlines()

knots = [(0,0)] * 10

seen_positions = set()
seen_positions.add(knots[-1])

sign = lambda x: -1 if x < 0 else (1 if x > 0 else 0)

for line in lines:

    direction, steps = line.split(' ')

    for _ in range(int(steps)):

        if direction == 'U':
            knots[0] = (knots[0][0], knots[0][1]+1)
        if direction == 'R':
            knots[0] = (knots[0][0]+1, knots[0][1])
        if direction == 'D':
            knots[0] = (knots[0][0], knots[0][1]-1)
        if direction == 'L':
            knots[0] = (knots[0][0]-1, knots[0][1])

        for i in range(1, len(knots)):

            dx = knots[i-1][0] - knots[i][0]
            dy = knots[i-1][1] - knots[i][1]

            if abs(dx) == 2 or abs(dy) == 2:
                knots[i] = (knots[i][0] + sign(dx), knots[i][1] + sign(dy))

        seen_positions.add(knots[-1])

print(len(seen_positions))
