#Task 1

#create 10x10 grid 
def create_grid():
    grid = [[0 for x in range(1000)] for y in range(1000)]
    return grid

grid = create_grid()

# read lines in txt file
def read_lines_txt():
    with open('input.txt') as f:
        lines = f.readlines()
    
    coord = []
    for val in lines:
        c = val.strip().split('->')
        list2=[]
        for val2 in c:
            list2.append( [int(x) for x in val2.split(',')]) 
        coord.append(list2)
    return coord


# for each coordinate pair, add 1 to grid
def fill_grdi():
    for val in coord:
        if val[0][0] == val[1][0]: # same x coords
            if val[0][1] < val[1][1]:
                for i in range(val[0][1], val[1][1]+1):
                    grid[i][val[0][0]] += 1
            else:
                for i in range(val[1][1], val[0][1]+1):
                    grid[i][val[1][0]] += 1 
        if val[0][1] == val[1][1]: #same y coords
            if val[0][0] < val[1][0]:
                for i in range(val[0][0], val[1][0]+1):
                    grid[val[0][1]][i] += 1
            else:
                for i in range(val[1][0], val[0][0]+1):
                    grid[val[1][1]][i] += 1
        

#count number of numbers above 1 in a grid
def count_grid():
    count = 0
    for i in range(1000):
        for j in range(1000):
            if grid[i][j] > 1:
                count += 1
    return count
        
grid = create_grid()   
coord = read_lines_txt()
fill_grdi()
count = count_grid()
print(count)


#Task 2

grid2 = create_grid()
coord2 = read_lines_txt()
