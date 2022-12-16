with open('input') as f:

    current_sum = 0
    max_sum = 0

    for line in f:

        line = line.strip()

        if line:
            current_sum += int(line)
        else:

            if current_sum > max_sum:
                max_sum = current_sum

            current_sum = 0

    if current_sum > max_sum:
        max_sum = current_sum

    print(max_sum)


# Alternative:
import itertools

# Read the file as individual lines
with open('input') as f:
    lines = f.read().splitlines()

# Split the lines on each separator
groups = [list(group) for key, group in itertools.groupby(lines, key=lambda row: row != '') if key]

# Convert the lines in each group to integers
groups = [[int(element) for element in group] for group in groups]

# Build the sum of each group
sums = [sum(group) for group in groups]

# Print the highest sum
print(max(sums))

# Conclusion:
# The vectorized version is maybe harder to decypher line-by-line for an uninitiated person,
# but it resembles more closely the way how a human would think about the problem.
# It seems also more extensible, as solving the second task only requires sorting the list of sums and printing the top 3 entries.
# One downside is that the code that is invoked is more complex and hidden behind some abstractions.
# Who really knows what's going on in itertools.groupby()?


# 1-liner solution of ChatGPT:
print(max([sum(list(map(int,line.split()))) for line in open('input').read().split('\n\n')]))

# Smart move to split the input file on \n\n, this avoids all the itertools madness
# The file is not properly closed, though


# Alternative, revisited:

# Read the file, split into groups
with open('input') as f:
    groups = f.read().split('\n\n')

# Convert the lines in each group to integers
groups = [[int(element) for element in group.splitlines()] for group in groups]

# Build the sum of each group
sums = [sum(group) for group in groups]

# Print the highest sum
print(max(sums))
