# Day 2: Rock Paper Scissors

# This code returns the correct solution for both parts of the puzzle
# To see the puzzle, go here:
# https://adventofcode.com/2022/day/2

# Part 1: Calculate total score

# if you didn't want me to hard code a dictionary, you shouldn't have made it only 9 entries :P
scoreDict = {
    "A X": 4,
    "A Y": 8,
    "A Z": 3,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 7,
    "C Y": 2,
    "C Z": 6
}

f = open("input2.txt", 'r')
lines: list[str] = f.readlines()
f.close()

score: int = 0
for line in lines:
    # we can aggregate the score with a dictionary lookup inside a one-liner
    score += int(scoreDict[line.strip()])

print(score)

# Part 2: calculate score by outcome

# again, it's just too easy to hardcode the "challenging" part of this problem
scoreDict2 = {
    "A X": 3,
    "A Y": 4,
    "A Z": 8,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 2,
    "C Y": 6,
    "C Z": 7
}

score2: int = 0
for line in lines:
    score2 += int(scoreDict2[line.strip()])

print(score2)

# This problem would have been more challenging if I didn't cheat - well, "cheat" - by writing a lookup table
# for both parts. At the same time, I don't think doing the calculations algorithmically would have been
# particularly elegant or satisfying, at least in this case. Sometimes a simple solution is a fine one.
# I definitely feel the difference made by my choice of tools here. I intentionally chose Python for this
# challenge because (a) I'm familiar with it and (b) it's much easier to problem solve with than some other
# languages. String handling, I/O, an extensive math library and flexible data structures are just some of
# the advantages I'm aware of right now. I'm looking forward to seeing other people's solutions to this
# problem, especially the more code-golf-y ones. That's where the real excitement lies. But personally, for
# a casual first timer, I'm satisfied with simply having got the answer. And what do they say about good coders?
# Laziness is a virtue.