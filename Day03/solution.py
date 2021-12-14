with open('Day03\input.txt') as f:
    lines = [x for x in f.read().splitlines()]

# Task 1
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

print(int(gamma, 2)*int(epsilon, 2))


#Task 2
# oxygen
l = lines.copy()

def counter(l, ind, threshold, one_or_zero):       
    ones_or_zeros = [val for val in l if int(val[ind]) == one_or_zero]
    count2 = [int(val[ind+1]) for val in ones_or_zeros].count(1)
    threshold = len(ones_or_zeros)/2
    return ones_or_zeros, threshold, count2

threshold = len(lines)/2 
count = [int(val[0]) for val in lines].count(1)
for ind in range(len(lines[0])-1):
    if threshold <= count:
        l, threshold, count = counter(l, ind, threshold, 1)
    else:
        l, threshold, count = counter(l, ind, threshold, 0)
        
for val in l:
    if int(val[(len(val)-1)]) == 1:
        oxygen_rating = int(val, 2)


#CO2
l = lines.copy()

def counter(l, ind, threshold, one_or_zero):       
    ones_or_zeros = [val for val in l if int(val[ind]) == one_or_zero]
    count2 = [int(val[ind+1]) for val in ones_or_zeros].count(1)
    threshold = len(ones_or_zeros)/2
    return ones_or_zeros, threshold, count2

threshold = len(lines)/2 
count = [int(val[0]) for val in lines].count(1)
for ind in range(len(lines[0])-1):
    if len(l)==1:
        break
    if threshold <= count:
        l, threshold, count = counter(l, ind, threshold, 0)
    else:
        l, threshold, count = counter(l, ind, threshold, 1)

co2_rating = int(l[0], 2)


print('life support rating: ', oxygen_rating*co2_rating)