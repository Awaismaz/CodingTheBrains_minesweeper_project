def minesweeper(A):
    row = len(A)
    for i in range(row):
        for j,e in enumerate(A[i]):
            if e != 'X':
                count = 0
                for k in range(i-1,i+2):
                    for l in range(j-1,j+2):
                        try:
                            if not(k == -1 or l == -1) and A[k][l] == 'X':
                                count += 1
                        except:
                            continue
                A[i] = A[i][:j] + str(count) + A[i][j+1:]
    return A

if __name__=="__main__":
    
    test = ["XOOXXXOO", 
            "OOOOXOXX", 
            "XXOXXOOO", 
            "OXOOOXXX", 
            "OOXXXXOX", 
            "XOXXXOXO", 
            "OOOXOXOX", 
            "OOXXOXOX"]

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

