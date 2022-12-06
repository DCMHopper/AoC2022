# Day 4: Camp Cleanup

# This code returns the correct solution for both parts of the puzzle
# To see the puzzle, go here:
# https://adventofcode.com/2022/day/4

# Part 1: Count pairs where one range contains the other

import re

f = open("input4.txt", 'r')
lines: list[str] = f.readlines()
f.close()

def line_to_list(line: str) -> list[int]:
    # we don't typecast this variable so we can reuse it for both strings and ints
    values = re.split("[, \-]", line)
    # just an excuse to use map
    values = map(int, values)
    # cast back to list since a map isn't actually helpful
    return list(values)

inclusions: int = 0
for line in lines:
    # using a single letter variable because I'm about to repeat it a lot
    r: list[int] = line_to_list(line)
    # one line!
    inclusions += ( (r[0] - r[2]) * (r[1] - r[3]) <= 0 )

print(inclusions)

# Part 2: Count ranges which overlap at all

intersections: int = 0
for line in lines:
    # another one liner coming up?
    r: list[int] = line_to_list(line)
    # you better believe it
    intersections += ( (r[0] - r[3]) * (r[1] - r[2]) <= 0 )

print(intersections)

# This was a fun puzzle. I enjoyed figuring out the set interactions in my head. Definitely
# was served well by math class in this one. Nothing else much to say - I suspect the string ops are
# still going to cost a lot of efficiency, but with input like this what can I do. (Use a different
# language, probably.)