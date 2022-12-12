# Day 8: Treetop Tree House

# This code returns the correct solution for both parts of the puzzle
# To see the puzzle, go here:
# https://adventofcode.com/2022/day/8

# the structure of the map we construct:
# a two-dimensional array
# where cells are a list of the form:
# [visible_left? visible_top? visible_right? visible_bottom?]
visibility_map: list[list[bool]] = [[]]
map: list[list[int]] = [[]]

# [ [[][][]]
#   [[][][]]
#   [[][][]] ]

# at first I tried to do processing at the same time as reading the input
# but it's better to split them up, at least when first writing the algo
f = open("input8.txt", 'r')
for char in f.read():
    if char == '\n':
        map.append([])
        visibility_map.append([])
    else:
        current_row = len(map) - 1
        map[current_row].append(int(char))
        visibility_map[current_row].append(False)

# input should be the line index, and a three char string:
# "[h,v][lr,rl]/[ud,du]"
def scan(line: int, dir: str) -> None:
    max_height: int = -1
    line_length = len(map[line]) if dir[0] == 'h' else len(map)
    current_height: int = -1
    current_index: tuple[int, int] = (0,0)
    for i in range(line_length):
        if dir == "hlr":
            current_index = (line, i)
        elif dir == "hrl":
            current_index = (line, (line_length - 1) - i)
        elif dir == "vud":
            current_index = (i, line)
        elif dir == "vdu":
            current_index = ((line_length - 1) - i, line)
        else:
            return
        current_height = map[current_index[0]][current_index[1]]
        # any tree higher than the ones before it will be visible from that direction
        if current_height > max_height:
            visibility_map[current_index[0]][current_index[1]] = True
            max_height = current_height

# I'm just modifying the visibility_map global array directly, and counting the hits inside
for i in range(len(map)):
    scan(i, "hlr")
    scan(i, "hrl")
for j in range(len(map[0])):
    scan(j, "vud")
    scan(j, "vdu")

visibles: int = 0
for line in visibility_map:
    for cell in line:
        if cell:
            visibles += 1

print(visibles)

# Part 2: find the highest possible "scenic score"

def directional_ss(x: int, y: int, dir: str) -> int:
    height = map[y][x]
    score: int = 0
    while 0 < y < len(map)-1 and 0 < x < len(map[y])-1:
        score+= 1
        # which direction we iterate in depends on the dir value
        if dir == "n": y -= 1
        elif dir == "s": y += 1
        elif dir == "e": x -= 1
        elif dir == "w": x += 1
        if map[y][x] >= height:
            break
    return score

# easiest to just get each cardinal direction separately and combine them here
def get_scenic_score(x: int, y: int) -> int:
    return ( directional_ss(x, y, "n") *
             directional_ss(x, y, "e") *
             directional_ss(x, y, "s") *
             directional_ss(x, y, "w") )

max_ss: int = 0
# we don't bother with trees on the rim, since one of their directional_ss values will be 0
for i in range(1, len(map)-1):
    for j in range(1, len(map[i])-1):
        current_ss = get_scenic_score(j,i)
        if current_ss > max_ss:
            max_ss = current_ss

print(max_ss)

# This solution is not as pretty as I'd hoped, but it functions in that all the information is in place.
# Some refactoring might be called for - changing some of these global variables into return values.
# I spent some time trying to do everything in 2 scans rather than 4 - I couldn't find a good way to
# handle visibility looking forward. I.e., if we're scanning a row left-to-right, how can we calculate
# visibility from the right during that scan? With no good answer, I just did two scans, one in each
# direction.