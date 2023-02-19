def minesweeper(A):
    R, C = len(A), len(A[0])
    result = [[""] * C for _ in range(R)]  # initialize the result array with empty strings
    for row in range(R):
        for col in range(C):
            if A[row][col] == "X":  # if the cell is a mine, set the result cell to "X"
                result[row][col] = "X"
            else:
                count = 0
                # loop through the neighbors of the cell
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        r, c = row + dr, col + dc
                        # if the neighbor cell is on the board and is a mine, increment the count
                        if (0 <= r < R) and (0 <= c < C) and (dr != 0 or dc != 0) and (A[r][c] == "X"):
                            count += 1
                if count == 0:
                    result[row][col] = "O"  # if the count is zero, set the result cell to "O"
                else:
                    result[row][col] = str(count)  # if the count is non-zero, set the result cell to the count
    return ["".join(row) for row in result]  # join the strings in each row to form the final result

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

