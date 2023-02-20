def minesweeper(A):
    #code that coverts the test matrix into desired output
    rows=len(A)
    col=len(A[0])
    A=[list(A[i])for i in range(rows)]
    for i in range(rows):
        for j in range(col):
            if not A[i][j]=='X':
                counter=0
                for k in range(i-1,i+2):
                    for l in range(j-1,j+2):
                        try:

                            if not (k==-1 or l==-1) and A[k][l]=='X':
                                counter+=1
                        except:
                            pass
                A[i][j]=str(counter)
    A=[''.join(A[i] for i in range(rows))]

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

