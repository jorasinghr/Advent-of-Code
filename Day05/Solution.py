#create 10x10 grid 
def create_grid():
    grid = [[0 for x in range(10)] for y in range(10)]
    return grid

grid = create_grid()

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

        


        
    
