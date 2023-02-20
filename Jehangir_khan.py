def minesweeper(A):
    rows = len(A)
    cols = len(A[0])
    A = [list(row) for row in A]
    for i in range(rows):
        for j in range(cols):
            if A[i][j] != 'X':
                counter = 0
                for k in range(max(i-1, 0), min(i+2, rows)):
                    for l in range(max(j-1, 0), min(j+2, cols)):
                        if A[k][l] == 'X':
                            counter += 1
                A[i][j] = str(counter)
    return [''.join(row) for row in A]  
    return A

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

