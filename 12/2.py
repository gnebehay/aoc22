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

distance[end_location[1], end_location[0]] = 0

current_locations = {end_location}
next_locations = set()

current_distance = 0

while current_locations:

    print(f'Current distance: {current_distance}')

    for location in current_locations:

        distance[location[1], location[0]] = current_distance

        height = heights[location[1], location[0]]

        print(f'Evaluating {location} of height {height}')

        candidate_locations = [
                (location[0], location[1]-1),
                (location[0], location[1]+1),
                (location[0]-1, location[1]),
                (location[0]+1, location[1])]

        for candidate_location in candidate_locations:

            print(f'Candidate step:{candidate_location}')

            if (
                    candidate_location[0] < 0 or
                    candidate_location[1] < 0 or
                    candidate_location[0] >= heights.shape[1] or
                    candidate_location[1] >= heights.shape[0]):

                print('Out of bounds')

                continue

            # Already visited?
            if not np.isinf(distance[candidate_location[1], candidate_location[0]]):
                print('Already visited')
                continue

            # Is it possible to ascend in the opposite direction?
            candidate_height = heights[candidate_location[1], candidate_location[0]]
            print(f'Height: {candidate_height}')
            if candidate_height + 1 < height:
                print('Height not right')
                continue

            # Are we done?
            if height == 0:
                print(f'Shortest distance is {current_distance}')
                
            # Because next_locations is a set, it is fine to add duplicate values here,
            # they will only be processed once
            next_locations.add(candidate_location)

    current_locations = next_locations
    next_locations = set()
    current_distance += 1

np.savetxt("distances.csv", distance.astype(int), delimiter="")
