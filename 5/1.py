def print_stacks():

    for i, stack in enumerate(stacks):
        print(f'{i+1} {stack}')

    print()

with open('input') as f:

    N = 9

    start_lines = []
    stacks = [[] for _ in range(N)]

    for i in range(8):
        start_lines.append(f.readline().strip())

    f.readline()
    f.readline()

    commands = f.read().splitlines()

start_lines.reverse()

for line in start_lines:

    for i in range(N):

        element = line[1+i*4]

        if element != ' ':
            stacks[i].append(element)

print_stacks()

for command in commands:

    print(command)

    command_tokens = command.split(' ')
    quantity = int(command_tokens[1])
    from_stack = int(command_tokens[3]) - 1
    to_stack = int(command_tokens[5]) - 1

    for i in range(quantity):
        stacks[to_stack].append(stacks[from_stack].pop())
        print_stacks()

for stack in stacks:
    print(stack[-1], end='')
print()
