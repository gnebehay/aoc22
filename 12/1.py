import string

import numpy as np
import pandas as pd

heights = pd.read_fwf('input', widths=[1]*136, header=None).values

start_location = np.where(heights == 'S')
start_location = (start_location[1][0], start_location[0][0])

end_location = np.where(heights == 'E')
end_location = (end_location[1][0], end_location[0][0])

heights[start_location[1], start_location[0]] = 'a'
heights[end_location[1], end_location[0]] = 'z'

heights = np.array([[string.ascii_lowercase.index(value) for value in row] for row in heights])
distance = np.full_like(heights, fill_value=np.inf, dtype=float)

distance[start_location[1], start_location[0]] = 0

current_locations = {start_location}
next_locations = set()

current_distance = 0

while current_locations:

    for location in current_locations:

        distance[location[1], location[0]] = current_distance

        height = heights[location[1], location[0]]

        candidate_locations = [
                (location[0], location[1]-1),
                (location[0], location[1]+1),
                (location[0]-1, location[1]),
                (location[0]+1, location[1])]

        for candidate_location in candidate_locations:

            if (
                    candidate_location[0] < 0 or
                    candidate_location[1] < 0 or
                    candidate_location[0] >= heights.shape[1] or
                    candidate_location[1] >= heights.shape[0]):

                continue

            # Already visited?
            if not np.isinf(distance[candidate_location[1], candidate_location[0]]):
                continue

            # Height too high?
            candidate_height = heights[candidate_location[1], candidate_location[0]]
            if candidate_height > height + 1:
                continue

            # Are we done?
            if candidate_location == end_location:
                print(f'Shortest distance is {current_distance+1}')
                
                # Stop processing
                candidate_locations = False
                break

            # Because next_locations is a set, it is fine to add duplicate values here,
            # they will only be processed once
            next_locations.add(candidate_location)

    current_locations = next_locations
    next_locations = set()
    current_distance += 1




### This is a solution that works for small inputs only.

#paths = [[start_location]]
#
#
#successful_paths = []
#
#
#while paths:
#
#    print(len(paths))
#
#    next_paths = []
#
#    for path in paths:
#
#        current_location = path[-1]
#
#        if current_location == end_location:
#            successful_paths.append(path)
#            print('Path found')
#            print(path)
#            continue
#
#        current_value = array[current_location[1], current_location[0]]
#
#        candidate_locations = [
#                (current_location[0], current_location[1]-1),
#                (current_location[0], current_location[1]+1),
#                (current_location[0]-1, current_location[1]),
#                (current_location[0]+1, current_location[1])]
#
#        for candidate_location in candidate_locations:
#
#            if (
#                    candidate_location[0] < 0 or
#                    candidate_location[1] < 0 or
#                    candidate_location[0] >= array.shape[1] or
#                    candidate_location[1] >= array.shape[0]):
#
#                continue
#
#            candidate_value = array[candidate_location[1], candidate_location[0]]
#            if candidate_value > current_value + 1:
#                continue
#
#            if candidate_location in path:
#                continue
#
#            next_path = path.copy()
#            next_path.append(candidate_location)
#
#            next_paths.append(next_path)
#
#            dead_end = False
#
#    paths = next_paths
#
