def minesweeper(A):
    matrix=A

    matrix.insert(len(matrix),'00000000')
    matrix.insert(0,'00000000')
    for idx,i in enumerate(matrix):
        matrix[idx]='0'+matrix[idx]+'0'

    temp = [list(string) for string in matrix]
    x=len(matrix)
    for j in range(1,x-1):
        for k in range(1,x-1):
            count=0
            if matrix[j][k]!='X':
                
                for q in range(3):
                    for r in range(3):
                        if q==1 and r==1:
                            pass
                        else:
                            if matrix[q+j-1][r+k-1]=='X':
                                count+=1
                temp[j][k]=str(count)

            else:
                pass
    temp1 = [''.join(string) for string in temp]
    temp1.pop(0)
    temp1.pop(-1)
    for idx,i in enumerate(temp1):
        temp1[idx]=temp1[idx].lstrip('0')
        temp1[idx]=temp1[idx].rstrip('0')
    return temp1


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
