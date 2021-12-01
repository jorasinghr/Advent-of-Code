
with open('Day01.txt') as f:
    lines = [int(x) for x in f.read().split()]

count = 0
for ind, val in enumerate(lines):
    if ind != 0 or ind != len(lines)-1:
        if val > lines[ind-1]:
            count += 1

print(count)