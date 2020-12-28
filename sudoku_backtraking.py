# this script will be using backtracking technique. 

sudoku_layout = [[0,0,2,9,8,0,5,0,0],
				 [4,0,0,0,7,0,0,1,3], 
				 [0,3,9,6,0,4,0,7,0], 
				 [2,0,0,0,5,6,4,0,0],
				 [8,4,0,3,0,0,2,0,1],
				 [9,0,7,0,0,1,0,8,6],
				 [6,0,0,7,0,5,1,3,0],
				 [0,9,1,4,0,0,0,0,5],
				 [0,2,0,0,3,0,6,0,8]]

def bt_solve(sudoku):
    find = find_empty(sudoku)
    if not find:
        return True # solved
    else:
        row, column = find
    
    for i in range(1,10):
        if is_valid(sudoku, (row,column), i): 
            sudoku[row][column] = i

            if bt_solve(sudoku):
                return True

            sudoku[row][column] = 0 # backtrack to remove the last element
    return False 

def is_valid(sudoku, coord, val):
    # check row
    for i in range(len(sudoku[0])):
        if sudoku[coord[0]][i] == val and coord[1] != i:
            return False

    # check column
    for i in range(len(sudoku[0])):
        if sudoku[i][coord[1]] == val and coord[0] != i:
            return False

    # check nonet
    nonet_x = coord[1]//3
    nonet_y = coord[0]//3
    for i in range(nonet_y*3,(nonet_y*3)+3):
        for j in range(nonet_x*3,(nonet_x*3)+3):
            if sudoku[i][j] == val and coord != (i,j):
                return False
    
    return True  

def print_layout(sudoku):
    for i in range(len(sudoku)):
        if i%3 ==  0 and i != 0:
            print("- - - - - - - - - - - - - ")
        
        for j in range(len(sudoku[0])):
            if j%3 == 0 and j != 0:
                print(" | ", end="")
            
            if j == 8: 
                print(sudoku[i][j])
            else:
                print(str(sudoku[i][j])+" ", end="")

def find_empty(sudoku):
    for i in range(len(sudoku)):
        for j in range(len(sudoku[0])):
            if sudoku[i][j] == 0:
                return (i,j) # row,column
    
    return None
 
print_layout(sudoku_layout)
bt_solve(sudoku_layout)
print("___________________________ ")
print("___________________________ ")
print_layout(sudoku_layout)