def minesweeper(A):
    
    rows = len(A)
    cols = len(A[0])
    A=[list(A[a]) for a in range(rows)]
    for i in range(rows):
        for j in range(cols):
            if  A[i][j] == 'O':
                count = 0
                for k in range(i-1,i+2):
                    for l in range(j-1,j+2):
                        try:
                            if k==-1 or l==-1:
                                pass
                            elif A[k][l] == 'X':
                                count+=1
                        except IndexError:
                            pass
                A[i][j] = str(count)

    A = [''.join(A[a]) for a in range(rows)]
                
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