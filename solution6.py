# Day 6: Tuning Trouble

# This code returns the correct solution for both parts of the puzzle
# To see the puzzle, go here:
# https://adventofcode.com/2022/day/6


# Part 1: Find first occurrence of 4 unique characters

def find_unique_substring(msg: str, msg_length: int) -> int:
    i = msg_length
    while len(set(msg[i-msg_length:i])) < msg_length and i <= len(msg): i += 1
    return i

# using 'with' calls __exit__() automatically, letting this sit on one line
with open("input6.txt", 'r') as input: packet: str = input.read()

print(find_unique_substring(packet, 4))

# Part 2: Find first occurrence of 14 unique characters

print(find_unique_substring(packet, 14))

# Simple problem today, so I spent a little time after solving cleaning it up. This would be a good one
# to target for a single line implementation.
# Lower level languages are more interesting for this one - I saw one solution using a bitmap
# to track which characters were inside the rolling "window" of 4 or 14, and return the solution
# once they were all unique. That raised a good optimization opportunity - when a duplicate char enters
# the frame, you can skip forward until the first copy of it exits again without bothering to check
# for uniqueness. IOW:
frame = "abcdefd" # duplicate 'd' enters
frame = "bcdefdg" # instead of proceding incrementally like this...
frame = "efdghij" # skip ahead until the first 'd' exits
# This task is also ripe for parallelization, segmenting the task among multiple threads and running
# them simultaneously. However, I'm happy with my ~6 line solution, and I'm going to keep it.