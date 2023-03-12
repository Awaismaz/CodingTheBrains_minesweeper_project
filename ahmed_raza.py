def minesweeper(A):
    #code that coverts the test matrix into desired output
    
    rows = len(A)  
    col = len(A[0])
    A = [list(A[a]) for a in range(rows)]

    for s in range(rows):
        for  t in range(col):
            if not A[s][t] == 'X':
                counter = 0
                for u in range(s-1,s+2):
                    for v in range(t-1,t+2):
                        try:
                            if not(u==-1 or  v==-1) and A[u][v] == 'X':
                                counter+=1
                        except:
                            pass        
                A[s][t] = str(counter)
    
    A = ["".join(A[a]) for a in range(rows)]
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

