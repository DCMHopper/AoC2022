# Day 1: Calorie Counting

# This code returns the correct solution for both parts of the puzzle
# To see the puzzle, go here:
# https://adventofcode.com/2022/day/1

# Part 1: Find the elf with the most calories, and return that calorie count

# read in calorie values
f = open('input1.txt', 'r')
lines: list[str] = f.readlines()
f.close()
currentElf, bestElf, currentCalories, maxCalories = 1, 1, 0, 0


for line in lines:
    if line != '\n':
        # this line is part of the current elf's total
        currentCalories += int(line.strip())
    else:
        # we're done counting for the current elf - check if it's the best and move on
        if(currentCalories > maxCalories):
            maxCalories = currentCalories
            bestElf = currentElf
        currentElf += 1
        currentCalories = 0

print(bestElf, " is the best elf, with ", maxCalories, " calories!")

# Part 2: Repeat, but for the top 3 elves summed

# define an ordered queue with arbitrary max length to contain the top n values
class topNQueue:
    def __init__(self, n: int):
        self.length = 0
        self.maxLength = n
        self.queue = []

    # if a candidate is larger than the smallest member, or the queue is not full yet, the candidate belongs
    def check_belonging(self, candidate: int) -> bool:
        if self.length < self.maxLength:
            return True
        if self.queue[self.length-1] < candidate:
            return True 
        return False

    # add_member will only actually add a new member if it belongs!
    def add_member(self, candidate: int) -> None:
        if self.check_belonging(candidate=candidate):
            if self.length < self.maxLength:
                self.queue.append(candidate)
                self.length += 1
            else:
                # find the appropriate index for the new candidate
                candidatePosition = self.length
                while candidatePosition > 0 and candidate > self.queue[candidatePosition - 1]:
                    candidatePosition -= 1
                self.queue.insert(candidatePosition, candidate)
                self.queue.pop(self.maxLength)
    def total(self) -> int:
        total: int = 0
        for item in self.queue:
            total += item
        return total

bestElves = topNQueue(3)

# similar to before, only now we're keeping track of the top 3 in bestElves
# we also no longer bother to keep track of which elf it is since that would involve tedious use of tuples
currentCalories = 0

for line in lines:
    if line != '\n':
        # this line is part of the current elf's total
        currentCalories += int(line.strip())
    else:
        # remember, we can call add_member even on calorie counts that are too small
        # the add_member function checks for belonging for us
        bestElves.add_member(currentCalories)
        currentCalories = 0

print("Combined, the best 3 elves have ", bestElves.total(), " calories between them")

# After finishing this problem, I went and looked at some other people's solutions.
# In retrospect, my solution is really bad! I'm wasting a lot of time keeping track of max values
# as we go, rather than waiting until the end to run a single sort().
# There's also no reason to keep track of the index of the best elf like I did in part 1.
# However, my code does have one advantage in that it could easily be modified to run over arbitrary
# user input, or extremely large datasets, without storing useless calorie counts of unworthy elves.
# This would save on runtime memory costs, which could be useful e.g. if we're crawling a large database.
# Maybe I can blame my inefficient algorithm on big data thinking poisoning my mind. Yeah, that's it.