class Node:

    def __init__(self, name, parent):

        self.size = 0
        self.children = []
        self.name = name
        self.parent = parent

    def total_size(self):

        children_size = 0

        for child in self.children:
            children_size += child.total_size()

        return self.size + children_size


overall_size = 0

def dfs(node):

    print('Entering ' + node.name)

    global overall_size

    for child in node.children:
        dfs(child)

    total_size = node.total_size()

    if total_size <= 100000:
        overall_size += total_size

    print('Leaving ' + node.name)

min_size_to_delete = float("inf")


def dfs2(node):

    print('Entering ' + node.name)

    global min_size_to_delete

    for child in node.children:
        dfs2(child)

    total_size = node.total_size()

    print(f'Total size: {total_size}')

    if total_size >= space_delta and total_size < min_size_to_delete:
        min_size_to_delete = total_size
        print(f'New min_size_to_delete: {min_size_to_delete}')

    print('Leaving ' + node.name)


with open('input') as f:
    lines = f.read().splitlines()

it = iter(lines)
line = next(it)

try:
    while True:

        assert(line[0] == '$')

        parts = line.split(' ')
        cmd = parts[1]

        if cmd == 'cd':

            print(line)

            arg = parts[2]

            if arg == '/':
                current_node = Node(name='/', parent=None)
                root = current_node
            elif arg == '..':
                current_node = current_node.parent
            else:
                new_node = Node(name=arg, parent=current_node)
                current_node.children.append(new_node)
                current_node = new_node

            line = next(it)

        if cmd == 'ls':

            line = next(it)

            while not line[0] == '$':

                print(line)

                dir_entry = line.split(' ')

                # Not sure if we really need to do anything here
                if dir_entry[0] == 'dir':
                    pass
                else:
                    current_node.size += int(dir_entry[0])

                line = next(it)


except StopIteration:
    print('End of file reached')

dfs(root)
print(overall_size)

total_disk_space = 70000000
space_required =   30000000
current_free_space = total_disk_space - root.total_size()
space_delta = space_required - current_free_space
assert space_delta > 0

print('DFS2')

dfs2(root)

print(root.total_size())
print(min_size_to_delete)
