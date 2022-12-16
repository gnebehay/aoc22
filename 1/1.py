with open('input.txt') as f:

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
