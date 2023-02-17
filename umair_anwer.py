def minesweeper(A):
    # code that coverts the test matrix into desired output
    row_len = len(A)
    col_len = len(A[0])
    # Splitting each string to character list
    A = [list(A[i]) for i in range(row_len)]

    # Iterating over the mine field
    for row in range(row_len):
        for col in range(col_len):
            # Check if position is a mine
            if(A[row][col] == 'X'):
                continue

            # Get all indices as tuples (row, col) for surrounding 8 positions of current position
            # Using list comprehension to generate tuples, in which all 8 possible surrounding positions are generated
            surround_list = [(row+i, col+j) for i in range(-1, 2) for j in range(-1, 2)]

            # Defining min and max bounds for rows and cols
            min_row = 0
            max_row = row_len-1
            min_col = 0
            max_col = col_len-1

            # Filter the list of surrounding positions such that all positions remain within bounds
            surround_list = list(filter(lambda pt: pt[0] >= min_row and pt[0] <= max_row and
                                        pt[1] >= min_col and pt[1] <= max_col, surround_list))

            # Iterating over the list of tuples of surrounding positions, and counting mines
            num_mines = 0
            for r_pos, c_pos in surround_list:
                if A[r_pos][c_pos] == 'X':
                    num_mines += 1

            # Update mines
            A[row][col] = str(num_mines)

    # Joining all characters back to strings
    A = [''.join(A[i]) for i in range(row_len)]

    return A


if __name__ == "__main__":

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
