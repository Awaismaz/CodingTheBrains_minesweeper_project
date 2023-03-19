def minesweeper(A):
    #code that coverts the test matrix into desired output
    
    rows = len(A)  
    cols = len(A[0])
    A = [list(A[a]) for a in range(rows)]    
    
    for b in range(rows):
        for c in range(cols):
            if not A[b][c] == 'X':
                counter = 0
                for d in range(max(0,b-1),min(rows,b+2)):
                    for e in range(max(0,c-1),min(cols,c+2)):
                        if A[d][e] == 'X':
                            counter += 1
                A[b][c] = str(counter)
    A = [''.join(A[f]) for f in range(rows)]
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

