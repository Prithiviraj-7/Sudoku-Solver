#checks for unassigned positions in the grid and returns False if grid is filled/solved
def is_empty(grid, pos):
    for c_row in range(9):
        for c_col in range(9):
            if grid[c_row][c_col] == 0:
                pos[0] = c_row
                pos[1] = c_col
                return True
    return False

#checks if the number to be assigned is already present in that row and returns false if it is present
def row_safe(grid, row, num):
    for i in range(9):
        if grid[row][i] == num:
             return False
    return True

#checks if the number to be assigned is already present in that colum and returns false if it is present
def col_safe(grid, col, num):
    for i in range(9):
        if grid[i][col] == num:
            return False
    return True

#checks if the number to be assigned is already present in that box and returns false if it is present
def box_safe(grid,row,col,num):
    box_row = row - row % 3
    box_col = col - col % 3

    for i in range(3):
        for j in range(3):
            if grid[i+box_row][j+box_col] == num:
                return False
    return True

#check if it is safe to assign the number in that position
def is_safe(grid,row,col,num):
     return row_safe(grid, row, num) and col_safe(grid, col, num) and box_safe(grid, row, col, num)

#solves the sudoku using backtracking
def solve(grid):
    pos = [0,0]  

    if not is_empty(grid,pos):
        return True

    row = pos[0]
    col = pos[1]

    for num in range(1,10):
        if is_safe(grid,row,col,num):
            grid[row][col] = num
            if solve(grid):
                return True
            grid[row][col] = 0         #backtracking

    return False






