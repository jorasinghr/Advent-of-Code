## Created with Github Copilot ##


#Task 1

#create 10x10 grid 
def create_grid(grid_size=1000):
    grid = [[0 for x in range(grid_size)] for y in range(grid_size)]
    return grid

# read lines in txt file
def read_lines_txt():
    with open('test_input.txt') as f:
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
def fill_grdi(coords):
    for val in coords:
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
def count_grid(grid_name, grid_size=1000):
    count = 0
    for i in range(grid_size):
        for j in range(grid_size):
            if grid_name[i][j] > 1:
                count += 1
    return count
        
grid = create_grid()   
fill_grdi(read_lines_txt())
#print(count_grid(grid))


#Task 2

grid2 = create_grid(10)
coord2 = read_lines_txt()

def fill_grdi2(coords):
    for val in coords:
        if val[0][0] == val[1][0]: # same x coords
            if val[0][1] < val[1][1]:
                for i in range(val[0][1], val[1][1]+1):
                    grid2[i][val[0][0]] += 1
            else:
                for i in range(val[1][1], val[0][1]+1):
                    grid2[i][val[1][0]] += 1 
        if val[0][1] == val[1][1]: #same y coords
            if val[0][0] < val[1][0]:
                for i in range(val[0][0], val[1][0]+1):
                    grid2[val[0][1]][i] += 1
            else:
                for i in range(val[1][0], val[0][0]+1):
                    grid[val[1][1]][i] += 1
                    
        if abs(val[0][0] - val[1][0]) == abs(val[0][1] - val[1][1]):
            #diagonal, if x1=y2 and x2=y1 its diagonal or if x1=y1 and x2=y2 its diagonal
            if val[0][0] > val[1][0]:
     
                if val[0][1] > val[1][1]:
                    print(1)
                    for i in range(0, val[0][0] - val[1][0] + 1):
                        grid2[val[0][0] - i][val[0][1] - i] += 1
                else:
                    print(2)
                    for i in range(0, val[0][0] - val[1][0] + 1):
                        grid2[val[0][0] - i][val[0][1] + i] += 1
                
            else:
                if val[0][1] > val[1][1]:
                    print(3)
                    for i in range(0, val[0][0] - val[1][0] + 1):
                        print(i)
                        grid2[val[0][0] + i][val[0][1] - i] += 1
                else:
                    print(4)
                    for i in range(0, val[0][0] - val[1][0] + 1):
                        grid2[val[0][0] + i][val[0][1] + i] += 1
                        
fill_grdi2(coord2)
print(count_grid(grid2, 10))