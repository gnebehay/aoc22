with open('input') as f:
    lines = f.read().splitlines()

count = 0

for line in lines:
    print(line)
    assignment1, assignment2 = line.split(',')
    assignment1 = assignment1.split('-')
    assignment2 = assignment2.split('-')

    assignment1 = (int(assignment1[0]), int(assignment1[1]))
    assignment2 = (int(assignment2[0]), int(assignment2[1]))

    print(assignment1)
    print(assignment2)

    if (assignment2[0] >= assignment1[0] and assignment2[1] <= assignment1[1]) or \
       (assignment1[0] >= assignment2[0] and assignment1[1] <= assignment2[1]):
        print('fully contained')
        count += 1

    print()

print(count)
