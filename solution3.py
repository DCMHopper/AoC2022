# Day 3: Rucksack Reorganization

# This code returns the correct solution for both parts of the puzzle
# To see the puzzle, go here:
# https://adventofcode.com/2022/day/3

# Part 1: Calculate sum of priorities of misplaced items

f = open("input3.txt", 'r')
lines: list[str] = f.readlines()
f.close()

def find_common_char(str1: str, str2: str) -> str:
    for c1 in str1:
        for c2 in str2:
            if c1 == c2:
                return c1
    return None

def eval_priority(char: str) -> int:
    # get the ascii number of the character, subtract 38 to place 'A' at 26,
    # then modulo 58 to make the lowercase letters wrap around
    # (not modulo 59 or we'd get 'a' == 0)
    return (ord(char) - 38) % 58

priority_score: int = 0
for line in lines:
    # midpoint is found by integer-dividing the length by 2
    compartment1 = line[:len(line)//2]
    compartment2 = line[len(line)//2:]
    priority_score += eval_priority(find_common_char(compartment1, compartment2))

print(priority_score)

# Part 2: Find common items among 3 unequal packs

# This time we'll use a recursive search function to iterate through an arbitrary length list of
# strings and return all matching characters at each level
def match_search(search_str: str, search_space: list[str]) -> str:
    # if we've popped all search_space strings, we've finished searching and we end the recursive loop
    if len(search_space) == 0:
        return search_str
    # this is mostly to make input a little more convenient
    if search_str == "":
        search_str = search_space.pop().strip()
    # thinking about this like breadth first search, where each subsequent string is another layer
    # of the search, our search frontier would be the next string in the list
    frontier: str = search_space.pop().strip()
    # any values in common between our search_str and the frontier will be held in 'matches'
    matches: str = ""
    for c1 in search_str:
        for c2 in frontier:
            # prune characters that aren't matches, or that we've already matched to
            if c1 == c2 and c1 not in matches:
                matches = matches + c1
    # yay tail recursion
    return match_search(matches, search_space)

priority_score = 0
for i in range(0, len(lines), 3):
    priority_score += eval_priority(match_search("",lines[i:i+3]))
print(priority_score)

# Today was a fun puzzle because I got to use tail-recursion. I went a little overboard for part 2,
# making a search function with more flexibility than necessary. It still lacks some things that would
# be required in the real world - error handling, input sanitzation, and gracefully resolving failure
# states.
# I'm also proud of the one-liner I came up with for converting from ASCII to puzzle score.
# It's a shame Python actually doesn't have a native char data type
# I did run into an error while writing match_search - my search_str was filling up with duplicate
# characters. I fixed it with the 'c1 not in matches' check, but there might be a better way.