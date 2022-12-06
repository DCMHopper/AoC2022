# Day 2: Rock Paper Scissors

# This code returns the correct solution for both parts of the puzzle
# To see the puzzle, go here:
# https://adventofcode.com/2022/day/2

# Part 1: Calculate total score

# if you didn't want me to hard code a dictionary, you shouldn't have made it only 9 entries :P
score_table = {
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
    score += int(score_table[line.strip()])

print(score)

# Part 2: calculate score by outcome

# again, it's just too easy to hardcode the "challenging" part of this problem
score_table2 = {
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
    score2 += int(score_table2[line.strip()])

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

# Update: I did see a clever solution I really liked:
arr1 = ["", "B X", "C Y", "A Z", "A X", "B Y", "C Z", "C X", "A Y", "B Z"]
arr2 = ["", "B X", "C X", "A X", "A Y", "B Y", "C Y", "C Z", "A Z", "B Z"]
# with these two arrays, the index of each string corresponds to the score value of that string. I did notice that
# scores were sequential and unique in my lookup tables, but I didn't think to encode it in such a concise manner.
# Is this practical in the real world? Probably not. An array like this is pretty low on semantic context to inform
# future readers of what its contents mean, and to be forward looking you'd have to be very confident that you won't
# have a future extension of the game that invalidates the constraints of uniqueness and completeness. Still, a
# very slick solution that compacts all the necessary information into a simpler data structure, and also
# reveals an interesting relationship between the two arrangements of scores.