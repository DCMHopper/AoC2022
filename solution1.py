# Day 1: Calorie Counting

# This code returns the correct solution for both parts of the puzzle
# To see the puzzle, go here:
# https://adventofcode.com/2022/day/1

# Part 1: Find the elf with the most calories, and return that calorie count

# read in calorie values
f = open('input1.txt', 'r')
lines: list[str] = f.readlines()
f.close()
current_elf, best_elf, current_calories, max_calories = 1, 1, 0, 0


for line in lines:
    if line != '\n':
        # this line is part of the current elf's total
        current_calories += int(line.strip())
    else:
        # we're done counting for the current elf - check if it's the best and move on
        if(current_calories > max_calories):
            max_calories = current_calories
            best_elf = current_elf
        current_elf += 1
        current_calories = 0

print(best_elf, " is the best elf, with ", max_calories, " calories!")

# Part 2: Repeat, but for the top 3 elves summed

# define an ordered queue with arbitrary max length to contain the top n values
class TopNQueue:
    def __init__(self, n: int):
        self.length = 0
        self.max_length = n
        self.queue = []

    # if a candidate is larger than the smallest member, or the queue is not full yet, the candidate belongs
    def check_belonging(self, candidate: int) -> bool:
        if self.length < self.max_length:
            return True
        if self.queue[self.length-1] < candidate:
            return True 
        return False

    # add_member will only actually add a new member if it belongs!
    def add_member(self, candidate: int) -> None:
        if self.check_belonging(candidate=candidate):
            if self.length < self.max_length:
                self.queue.append(candidate)
                self.length += 1
            else:
                # find the appropriate index for the new candidate
                candidate_position = self.length
                while candidate_position > 0 and candidate > self.queue[candidate_position - 1]:
                    candidate_position -= 1
                self.queue.insert(candidate_position, candidate)
                self.queue.pop(self.max_length)
    def total(self) -> int:
        total: int = 0
        for item in self.queue:
            total += item
        return total

best_elves = TopNQueue(3)

# similar to before, only now we're keeping track of the top 3 in best_elves
# we also no longer bother to keep track of which elf it is since that would involve tedious use of tuples
current_calories = 0

for line in lines:
    if line != '\n':
        # this line is part of the current elf's total
        current_calories += int(line.strip())
    else:
        # remember, we can call add_member even on calorie counts that are too small
        # the add_member function checks for belonging for us
        best_elves.add_member(current_calories)
        current_calories = 0

print("Combined, the best 3 elves have ", best_elves.total(), " calories between them")

# After finishing this problem, I went and looked at some other people's solutions.
# In retrospect, my solution is really bad! I'm wasting a lot of time keeping track of max values
# as we go, rather than waiting until the end to run a single sort().
# There's also no reason to keep track of the index of the best elf like I did in part 1.
# However, my code does have one advantage in that it could easily be modified to run over arbitrary
# user input, or extremely large datasets, without storing useless calorie counts of unworthy elves.
# This would save on runtime memory costs, which could be useful e.g. if we're crawling a large database.
# Maybe I can blame my inefficient algorithm on big data thinking poisoning my mind. Yeah, that's it.