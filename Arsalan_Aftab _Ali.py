import numpy as np

def minesweeper(A):
    #code that coverts the test matrix into desired output
    rows = len(A)
    cols = len(A[0])

    grid = [list(A[i]) for i in range(rows)]
    grid = np.pad(grid, pad_width=1, mode='constant', constant_values='0')
    
    # We are adding 1 to the rows and columns because our rows length equals 8 before padding and we need to iterate from 1 till 8 and in range function the last number is 
    # not included, so we need to add 1 to the rows and columns and that equal rows and cols = 9 so now the range function will iterate from 1 to 8(exluding 9)
    for i in range(rows+1):
        for j in range(cols+1):
            count = 0
            if grid[i][j] == "X":
                continue
            if grid[i][j] == "O" and grid[i-1][j-1] == "X":
                count = count + 1
            if grid[i][j] == "O" and grid[i-1][j] == "X":
                count = count + 1
            if grid[i][j] == "O" and grid[i-1][j+1] == "X":
                count = count + 1
            if grid[i][j] == "O" and grid[i][j-1] == "X":
                count = count + 1
            if grid[i][j] == "O" and grid[i][j+1] == "X":
                count = count + 1
            if grid[i][j] == "O" and grid[i+1][j-1] == "X":
                count = count + 1
            if grid[i][j] == "O" and grid[i+1][j] == "X":
                count = count + 1
            if grid[i][j] == "O" and grid[i+1][j+1] == "X":
                count = count + 1     
            
            grid[i][j] = str(count)
    
    # This will replace all the 0's with empty strings
    grid = np.where(grid == "0", "", grid)

    # This will convert this grid into a list of strings 
    grid = ["".join(grid[i]) for i in range(1, rows+1) and range(1, cols+1)]
    
    return grid

if __name__=="__main__":
    
    test = ["XOOXXXOO", 
            "OOOOXOXX", 
            "XXOXXOOO", 
            "OXOOOXXX", 
            "OOXXXXOX", 
            "XOXXXOXO", 
            "OOOXOXOX", 
            "XOXXOXOX"]

    """Desired Output is as under
    
    ["X11XXX32", 
     "3335X5XX", 
     "XX3XX554", 
     "3X556XXX", 
     "24XXXX6X", 
     "X3XXX5X3", 
     "245X6X5X", 
     "X2XX4X4X"]
    """

    print(minesweeper(test))

