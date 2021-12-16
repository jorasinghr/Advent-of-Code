def matrix_import():
    with open('Day04/input.txt') as f:
        first_line = f.readline().split(',')
        first_line = [int(val) for val in first_line] #bingo values
        lines = f.readlines()

    #Clean-up to get the boards in preffered format
    l=[]    
    for val in lines:
        if val != '\n':
            l.append(val.replace('\n', ''))

    def matrix_op(l, ind):
        matrix = list(filter(None, l[ind].split(' ')))
        matrix = [int(val) for val in matrix]
        return matrix

    matrices = []
    for ind in range(0, len(l), 5):
        matrix = []
        for inner_ind in range(0,5):
            matrix.append(matrix_op(l, ind+inner_ind))
        matrices.append(matrix)
    return first_line, matrices
    
first_line, matrices = matrix_import()

# Task 1
board_winner = False
break_value = False
for bingo_nr in first_line:
    if break_value:
        break  
    for board_nr, board in enumerate(matrices): #iterating each board
        if break_value:
            break
        for row, line in enumerate(board): # iterating each line in each board
            if break_value:
                break
            for col, number in enumerate(line):
                #print(ind+ind1)
                #print(matrices[board_nr][3][0] )
                if number == bingo_nr:
                    matrices[board_nr][row][col] = -1
                    
                    if sum(matrices[board_nr][row]) == -5:
                        board_winner = board_nr
                        break_value = True
                        bingo_winner = bingo_nr
                        break
                        
                    elif (matrices[board_nr][0][col] + 
                            matrices[board_nr][1][col] + 
                            matrices[board_nr][2][col] + 
                            matrices[board_nr][3][col] +
                            matrices[board_nr][4][col]) == -5:
                        board_winner = board_nr
                        bingo_winner = bingo_nr
                        break_value = True
                        break


board_count = 0
for val in matrices[board_winner]:
    for number in val:
        if number != -1:
            board_count += number 
            
print(board_count*bingo_winner)


# Task 2

first_line, matrices = matrix_import()
winner_boards = []
break_value = False
for bingo_nr in first_line:
    if break_value:
        break  
    for board_nr, board in enumerate(matrices): #iterating each board
        if break_value:
            break
        for row, line in enumerate(board): # iterating each line in each board
            if break_value:
                break
            for col, number in enumerate(line):
                if number == bingo_nr:
                    matrices[board_nr][row][col] = -1
                    if sum(matrices[board_nr][row]) == -5:
                        if not board_nr in winner_boards:
                            winner_boards.append(board_nr)
                        if len(winner_boards) == len(matrices):
                            break_value = True
                            bingo_winner = bingo_nr
                            break
                        
                    elif (matrices[board_nr][0][col] + 
                            matrices[board_nr][1][col] + 
                            matrices[board_nr][2][col] + 
                            matrices[board_nr][3][col] +
                            matrices[board_nr][4][col]) == -5:
                        if not board_nr in winner_boards:
                            winner_boards.append(board_nr)
                        if len(winner_boards) == len(matrices):
                            break_value = True
                            bingo_winner = bingo_nr
                            break

board_loser = winner_boards[-1]

board_count = 0
for val in matrices[board_loser]:
    for number in val:
        if number != -1:
            board_count += number 
            
print(board_count*bingo_winner)
