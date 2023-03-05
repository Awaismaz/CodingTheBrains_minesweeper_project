def minesweeper(A):
    #code that coverts the test matrix into desired output
    boardSize=len(A)
    tempRow=""
    count=0
    for i in range(boardSize):
        for j in range(boardSize):
            if A[i][j]=='O':
                if A[i][j-1]=='X' and (j-1) >= 0: #
                    count+=1
                if (j+1) < boardSize:
                    if A[i][j+1]=='X':
                        count+=1
                if A[i-1][j]=='X' and (i-1) >= 0: #
                    count+=1
                if (i+1) < boardSize:
                    if A[i+1][j]=='X':
                        count+=1
                if A[i-1][j-1]=='X' and (i-1) >= 0 and (j-1) >= 0: #
                    count+=1
                if (j+1) < boardSize:
                    if A[i-1][j+1]=='X' and (i-1) >=0:
                        count+=1
                if (i+1) < boardSize:
                    if A[i+1][j-1]=='X' and (j-1) >= 0:
                        count+=1
                if (i+1) < boardSize and (j+1) < boardSize:
                    if A[i+1][j+1]=='X':
                        count+=1
                tempRow=tempRow+str(count)
            else:
                tempRow=tempRow+'X'
            count=0
        A[i]=tempRow
        tempRow=""
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

