def minesweeper(A):
    #code that coverts the test matrix into desired output
    rows = len(A)
    cols = len(A[0])

    grid = [list(A[i]) for i in range(cols)]
    for i in range(rows):
        for j in range(cols):
            count = 0
            if grid[i][j] == "X":
                continue
            if grid[i][j] == "O" and grid[i-1][j-1] == "X":
                    count = count + 1
            if grid[i-1][j] == "O" and grid[i-1][j] == "X":
                    count = count + 1
            if grid[i-1][j] == "O" and grid[i-1][j+1] == "X":
                    count = count + 1
            if grid[i-1][j] == "O" and grid[i][j-1] == "X":
                    count = count + 1
            if grid[i-1][j] == "O" and grid[i][j+1] == "X":
                    count = count + 1
            if grid[i-1][j] == "O" and grid[i+1][j-1] == "X":
                    count = count + 1
            if grid[i-1][j] == "O" and grid[i+1][j] == "X":
                    count = count + 1
            if grid[i-1][j] == "O" and grid[i+1][j+1] == "X":
                    count = count + 1    
             
            grid[i][j]= count
    
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

