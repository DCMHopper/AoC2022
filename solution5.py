# Day 5: Supply Stacks

# This code returns the correct solution for both parts of the puzzle
# To see the puzzle, go here:
# https://adventofcode.com/2022/day/5

from typing import Tuple
import itertools

# Part 1: Find the crates which wind up on top

# read method is a little bit more complicated this time - luckily
# every crate is a single character right now so we can just grab every 4th char without actually parsing brackets
def lineToList(line: str) -> list[str]:
    crateList: list[str] = []
    for i in range(1, len(line), 4):
        crateList.append(line[i])
    return crateList

# I'm going to define this custom class of a collection of stacks for ease of use
class StackCluster:
    def __init__(self, numStacks: int) -> None:
        self.stacks = [[] for i in range(numStacks)]
    
    def addCrate(self, crate: str, position: int) -> None:
        if crate != " ":
            self.stacks[position].append(crate)

    def grabCrate(self, position: int) -> str:
        return self.stacks[position].pop()

    # these two methods extend the class for part 2
    def addCrates(self, crates: list[str], position: int) -> None:
        for crate in crates:
            if crate != " ":
                self.stacks[position].append(crate)
    
    def grabCrates(self, position: int, howMany: int) -> list[str]:
        crates: list[str] = []
        for _ in itertools.repeat(None, howMany):
            crates.append(self.stacks[position].pop())
        crates.reverse()
        return crates

    def getTopCrates(self) -> list[str]:
        tops: str = ""
        for stack in self.stacks:
            tops += stack[len(stack)-1]
        return tops


f = open("input5.txt", 'r')
config,moves = [],[]
while (line := f.readline()) != "\n":
    config.append(lineToList(line))
config.reverse()
moves = f.readlines()
f.close()

# hardcoded 9 for now bc lazy
stackCluster = StackCluster(9)
# skip the first line (stack labels)
for i in range(1,len(config)):
    for j in range(len(config[i])):
        # these loops don't feel very pythonic but what do I care- er, know. what do I know
        stackCluster.addCrate(config[i][j], j)

def parseMove(move: str) -> Tuple[int, int, int]:
    tokens = move.split()
    # more hard coding, every move instruction is of the form:
    # ['move', 'X', 'from', 'Y', 'to', 'Z']
    # even more ugliness from the '-1's to bring us back into 0-indexing
    instruction: Tuple[int, int, int] = (int(tokens[1]), int(tokens[3])-1, int(tokens[5])-1)
    return instruction

def execute(instruction: Tuple[int, int, int], stackCluster: StackCluster) -> None:
    # trying to be a little pythony with the iterable and empty var here
    for _ in itertools.repeat(None, instruction[0]):
        stackCluster.addCrate(stackCluster.grabCrate(instruction[1]), instruction[2])

for move in moves:
    execute(parseMove(move),stackCluster)
print(stackCluster.getTopCrates())

# Part 2: grab N crates at once, rather than one after another

stackCluster2 = StackCluster(9)
for i in range(1,len(config)):
    for j in range(len(config[i])):
        stackCluster2.addCrate(config[i][j], j)

def goldExecute(instruction: Tuple[int, int, int], stackCluster: StackCluster) -> None:
    stackCluster.addCrates(stackCluster.grabCrates(instruction[1], instruction[0]), instruction[2])

for move in moves:
    goldExecute(parseMove(move),stackCluster2)
print(stackCluster2.getTopCrates())

# This one turned out to be a total mess. Ugly, hard to read, and idologically inconsistent. However, having
# gotten the right answer for both parts, I can't say I'm motivated to clean it up.
# One thing I only realized today is I've been camelCasing my variables when Python's norm is to snake_case.
# I thought something felt weird. Now I'm faced with a dilemma: go back in time, and clean up my previous
# solutions, or continue with this breach of decorum. I'll probably do the former - I'm trying to become
# more Pythonic, not less.
# Speaking of which, tomorrow I'm going to lean in to making everything an iterable - some of
# my loops today were not pretty. Next time I define a data type I'll try to give it a __next__ function.
# Also: @@#%* string parsing.