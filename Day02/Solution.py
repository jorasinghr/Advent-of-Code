###Advent of Code###
with open('Day02\input.txt') as f:
    lines = [x for x in f.read().splitlines()]

# Task 1
depth = 0
horizontal_pos = 0
for id, val in enumerate(lines):
    move, num = val.split()
    if move == 'forward':
        horizontal_pos += int(num)
    elif move == 'up':
        depth -= int(num)
    elif move == 'down':
        depth += int(num)
    else:
        print('ERROR!')

print('Horizontal position multiplied with depth =', depth*horizontal_pos)


# Task 2
depth = 0
horizontal_pos = 0
aim = 0

for id, val in enumerate(lines):
    move, num = val.split()
    num = int(num)
    if move == 'forward':
        horizontal_pos += num
        depth += aim*num
    elif move == 'up':
        aim -= num
    elif move == 'down':
        aim += num
    else:
        print('ERROR!')

print('Horizontal position multiplied with depth =', depth*horizontal_pos)
