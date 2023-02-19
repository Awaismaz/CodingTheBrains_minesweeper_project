def minesweeper(A):
    length_of_rows = len(A)
    length_of_columns = len(A[1])
    result = [list(y) for y in A]

    
    for i in range(length_of_rows):#rows
        for j in range(length_of_columns):#columns
            if A[i][j]=='X':
                result[i][j] = 'X'
            else:
                mines = 0
                r = [max(0,i-1),min(i+2,length_of_rows),max(0,j-1),min(j+2,length_of_columns)]
                for k in range(r[0],r[1]):
                    for l in range(r[2],r[3]):
                        if A[k][l]=='X':
                            mines=mines+1
                if mines==0:
                    result[i][j]='0'
                else:
                    result[i][j] = str(mines)
    
    return result
    

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

