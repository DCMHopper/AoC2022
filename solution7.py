# Day 7: Tuning Trouble

# This code returns the correct solution for both parts of the puzzle
# To see the puzzle, go here:
# https://adventofcode.com/2022/day/7

from __future__ import annotations
from typing import Union

# Part 1: Find sum of small directories

# a class for directories, with a list of children and (potentially) a parent node
class Dir:
    def __init__(self, name: str, parent: Dir = None) -> None:
        self.name = name
        self.size: int = 0
        self.children: list[Union[Dir, Doc]] = []
        self.parent = parent

    # children can be either a Dir or a Doc
    def add_child(self, node: Union[Dir, Doc]) -> None:
        self.children.append(node)

    # propogate this up the parent chain!
    def update_size(self, new_weight: int) -> None:
        self.size += new_weight
        if self.parent is not None:
            self.parent.update_size(new_weight)

    # mostly for debugging
    def print_tree(self) -> None:
        print("dir:", self.name, ": ", self.size)
        for child in self.children:
            child.print_tree()

    # less human-readable, but more machine-readable tree crawl
    def dir_sizes(self) -> str:
        log: list[tuple[str, int]] = [(self.name, self.size)]
        for child in self.children:
            if isinstance(child, Dir):
                log += child.dir_sizes()
        return log

    def __repr__(self) -> str:
        return "Directory: " + self.name

# documents come into this world with a size already - when we create a new document,
# we have to update_size() its parent as well
# also docs are not allowed to be parentless, unlike root
class Doc:
    def __init__(self, name: str,  parent: Dir, size: int = 0) -> None:
        self.name = name
        self.parent = parent
        self.parent.update_size(size)
        self.size = size

    def print_tree(self) -> None:
        print("doc:", self.name, ": ", self.size)

    def __repr__(self) -> str:
        return "File: " + self.name

root: Dir = Dir("/")
wd = root # working directory

# we execute commands on lines with a leading $
def exec_cmd(wd: Dir, command: str) -> Dir:
    if command == "ls":
        # we already assume that any non-command lines are output from ls, so no need to
        # enter a new state here
        return wd
    cd_arg: str = command.split(" ")[1]
    if cd_arg == "/":
        return root
    elif cd_arg == "..":
        return wd.parent
    else:
        for child in wd.children:
            # what a clunky way to find a child node! anyways -
            if child.name == cd_arg:
                return child

# the only non-$ lines (as mentioned above) are output from ls
def read_in(wd: Dir, entry: str) -> Dir:
    desc, name = entry.split(" ")
    if desc == "dir":
        # define a new directory in the current workind directory
        wd.add_child(Dir(name, parent=wd))
    else:
        wd.add_child(Doc(name, wd, int(desc)))
    return wd

f = open("input7.txt", 'r')
for line in f.readlines():
    # I don't want to think about newlines right now
    line = line.strip()
    if line[0] == "$":
        # grab everything past the '$ '
        wd = exec_cmd(wd, line[2:])
    else:
        wd = read_in(wd, line)

part1: int = 0
tree = root.dir_sizes()
for directory in tree:
    if directory[1] <= 100000:
        part1 += directory[1]

print(part1)

# Part 2: find smallest acceptable directory to delete
REQ_SPACE = tree[0][1] - 40000000 # root size - max allowed
smallest_valid_dir_size = tree[0][1]
for directory in tree:
    if REQ_SPACE <= directory[1] < smallest_valid_dir_size:
        smallest_valid_dir_size = directory[1]

print(smallest_valid_dir_size)

# The part 1 descriptions specifies that nested small directories should count more than once
# maybe this is just a concession to problem difficulty but I think it's dumb. Anyways.
# This is far from the most efficient file system - for that I think I would have to use a hash map?
# Not completely sure, but I know my tree of linked objects is going to be slow traversing.
# Fortunately I only parse it once.
# It would be more efficient if I could do everything in a single pass, rather than *first* building
# the tree and *then* reading sizes. however, that comes with its own problems - I'd have to define a
# frontier of directories that are not fully explored yet, and I don't have control over what order
# the input browses files in - it's safer to assume nothing until the end of the input file, imo.
# Fortunately, once the tree is built, the rest of each problem is trivial. Part 1 took me over an
# hour to put together, part 2 was an additional 5 minutes.
# This problem was a step up in challenge from the previous ones, which I'm grateful for.
# One other area I could improve: my parsing is not very systematic. It works for the limited input
# I have now, but string parsing is happening in both my main loop and my exec_cmd() function -
# in a perfect world, exec_cmd would be called with command values, in data types most useful to
# the function. Something like exec_cmd(command: str, args: list)