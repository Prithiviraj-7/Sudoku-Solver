def print_grid(grid):
    for i in range(9):
        for j in range(9):
            print(grid[i][j], end = " ")
        print("")

# function to check for unassigned position and returns false if there are no unassigned positions
def is_empty(grid, pos):
    for c_row in range(9):
        for c_col in range(9):
            if grid[c_row][c_col] == 0:
                pos[0] = c_row
                pos[1] = c_col
                return True
    return False

def row_safe(grid, row, num):
    for i in range(9):
        if grid[row][i] == num:
             return False
    return True

def col_safe(grid, col, num):
    for i in range(9):
        if grid[i][col] == num:
            return False
    return True

def box_safe(grid,row,col,num):
    box_row = row - row % 3
    box_col = col - col % 3

    for i in range(3):
        for j in range(3):
            if grid[i+box_row][j+box_col] == num:
                return False
    return True

def is_safe(grid,row,col,num):
     return row_safe(grid, row, num) and col_safe(grid, col, num) and box_safe(grid, row, col, num)

def solver(grid):
    pos = [0,0]

    if not is_empty(grid,pos):
        return True

    row = pos[0]
    col = pos[1]

    for num in range(1,10):
        if is_safe(grid,row,col,num):
            grid[row][col] = num
            if solver(grid):
                return True
            grid[row][col] = 0

    return False

if __name__ == "__main__":

    grid = [[0 for i in range(9)] for j in range(9)]

    grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
          [5, 2, 0, 0, 0, 0, 0, 0, 0],
          [0, 8, 7, 0, 0, 0, 0, 3, 1],
          [0, 0, 3, 0, 1, 0, 0, 8, 0],
          [9, 0, 0, 8, 6, 3, 0, 0, 5],
          [0, 5, 0, 0, 9, 0, 6, 0, 0],
          [1, 3, 0, 0, 0, 0, 2, 5, 0],
          [0, 0, 0, 0, 0, 0, 0, 7, 4],
          [0, 0, 5, 2, 0, 6, 3, 0, 0]]

    if solver(grid):
        print_grid(grid)
    else:
        print("No Solution exists")




