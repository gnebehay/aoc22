with open('input') as f:
    lines = f.read().splitlines()

values = [1]

for line in lines:

    parts = line.split(' ')

    values.append(values[-1])

    if len(parts) == 2:
        values.append(values[-1] + int(parts[1]))

print(values[19]*20 + values[59]*60 + values[99]*100 + values[139]*140 + values[179]*180 + values[219]*220)

