with open('Day03\input.txt') as f:
    lines = [x for x in f.read().splitlines()]


gamma = ''
epsilon = ''
for ind in range(len(lines[0])):
    threshold = len(lines)/2
    count = [int(val[ind]) for val in lines].count(1)

    if threshold < count:
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'

print(int(gamma, 2)*int(epsilon,2))
