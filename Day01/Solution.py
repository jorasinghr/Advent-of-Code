###Advent of Code###
with open('Day01\input.txt') as f:
    lines = [int(x) for x in f.read().split()]

# task 1
count = 0
for ind, val in enumerate(lines):
    if ind != 0 or ind != len(lines) - 1:
        if val > lines[ind - 1]:
            count += 1

print('Task 1:', count)

# task 2
count = 0
for ind, val in enumerate(lines):
    if ind < len(lines) - 3:
        A = val + lines[ind + 1] + lines[ind + 2]
        B = lines[ind + 1] + lines[ind + 2] + lines[ind + 3]
        if B > A:
            count += 1

print('Task 2:', count)
