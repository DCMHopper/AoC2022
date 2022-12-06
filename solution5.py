# Day 5: Supply Stacks

# This code returns the correct solution for both parts of the puzzle
# To see the puzzle, go here:
# https://adventofcode.com/2022/day/5

from typing import Tuple
import itertools

# Part 1: Find the crates which wind up on top

# read method is a little bit more complicated this time - luckily
# every crate is a single character right now so we can just grab every 4th char without actually parsing brackets
def line_to_list(line: str) -> list[str]:
    crate_list: list[str] = []
    for i in range(1, len(line), 4):
        crate_list.append(line[i])
    return crate_list

# I'm going to define this custom class of a collection of stacks for ease of use
class StackCluster:
    def __init__(self, num_stacks: int) -> None:
        self.stacks = [[] for i in range(num_stacks)]
    
    def add_crate(self, crate: str, position: int) -> None:
        if crate != " ":
            self.stacks[position].append(crate)

    def grab_crate(self, position: int) -> str:
        return self.stacks[position].pop()

    # these two methods extend the class for part 2
    def add_crates(self, crates: list[str], position: int) -> None:
        for crate in crates:
            if crate != " ":
                self.stacks[position].append(crate)
    
    def grab_crates(self, position: int, how_many: int) -> list[str]:
        crates: list[str] = []
        for _ in itertools.repeat(None, how_many):
            crates.append(self.stacks[position].pop())
        crates.reverse()
        return crates

    def get_top_crates(self) -> list[str]:
        tops: str = ""
        for stack in self.stacks:
            tops += stack[len(stack)-1]
        return tops


f = open("input5.txt", 'r')
config,moves = [],[]
while (line := f.readline()) != "\n":
    config.append(line_to_list(line))
config.reverse()
moves = f.readlines()
f.close()

# hardcoded 9 for now bc lazy
stack_cluster = StackCluster(9)
# skip the first line (stack labels)
for i in range(1,len(config)):
    for j in range(len(config[i])):
        # these loops don't feel very pythonic but what do I care- er, know. what do I know
        stack_cluster.add_crate(config[i][j], j)

def parse_move(move: str) -> Tuple[int, int, int]:
    tokens = move.split()
    # more hard coding, every move instruction is of the form:
    # ['move', 'X', 'from', 'Y', 'to', 'Z']
    # even more ugliness from the '-1's to bring us back into 0-indexing
    instruction: Tuple[int, int, int] = (int(tokens[1]), int(tokens[3])-1, int(tokens[5])-1)
    return instruction

def execute(instruction: Tuple[int, int, int], stack_cluster: StackCluster) -> None:
    # trying to be a little pythony with the iterable and empty var here
    for _ in itertools.repeat(None, instruction[0]):
        stack_cluster.add_crate(stack_cluster.grab_crate(instruction[1]), instruction[2])

for move in moves:
    execute(parse_move(move),stack_cluster)
print(stack_cluster.get_top_crates())

# Part 2: grab N crates at once, rather than one after another

stack_cluster2 = StackCluster(9)
for i in range(1,len(config)):
    for j in range(len(config[i])):
        stack_cluster2.add_crate(config[i][j], j)

def gold_execute(instruction: Tuple[int, int, int], stack_cluster: StackCluster) -> None:
    stack_cluster.add_crates(stack_cluster.grab_crates(instruction[1], instruction[0]), instruction[2])

for move in moves:
    gold_execute(parse_move(move),stack_cluster2)
print(stack_cluster2.get_top_crates())

# This one turned out to be a total mess. Ugly, hard to read, and idologically inconsistent. However, having
# gotten the right answer for both parts, I can't say I'm motivated to clean it up.
# One thing I only realized today is I've been camelCasing my variables when Python's norm is to snake_case.
# I thought something felt weird. Now I'm faced with a dilemma: go back in time, and clean up my previous
# solutions, or continue with this breach of decorum. I'll probably do the former - I'm trying to become
# more Pythonic, not less.
# Speaking of which, tomorrow I'm going to lean in to making everything an iterable - some of
# my loops today were not pretty. Next time I define a data type I'll try to give it a __next__ function.
# Also: @@#%* string parsing.