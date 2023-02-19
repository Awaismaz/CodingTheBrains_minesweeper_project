def minesweeper(A):
    #code that coverts the test matrix into desired output
    result = []
    for i in range(len(A)):
        values = A[i]
        resultStr = ''
        for j in range(len(values)):
            count = 0
            if values[j] == 'O':
                if j == len(values)-1:
                    if values[j-1] == 'X':
                        count += 1
                elif j == 0:
                    if values[j+1] == 'X':
                        count +=1
                else:
                    if values[j-1] == 'X':
                        count +=1
                    if values[j+1] == 'X':
                        count +=1
                if i == 0:
                    if A[i+1][j] == 'X':
                        count += 1
                    if j == 0:
                        if A[i+1][j+1] == 'X':
                            count += 1
                    elif j == len(values) -1:
                        if A[i+1][j-1] == 'X':
                            count += 1
                    else:
                        if A[i+1][j+1] == 'X':
                            count += 1
                        if A[i+1][j-1] == 'X':
                            count += 1
                elif i == len(A)-1:
                    if A[i-1][j] == 'X':
                        count  += 1
                    if j == 0:
                        if A[i-1][j+1] == 'X':
                            count += 1
                    elif j == len(values) -1:
                        if A[i-1][j-1] == 'X':
                            count += 1
                    else:
                        if A[i-1][j+1] == 'X':
                            count += 1
                        if A[i-1][j-1] == 'X':
                            count += 1
                else:
                    if A[i+1][j] == 'X':
                        count += 1
                    if A[i-1][j] == 'X':
                        count  += 1
                    if j == len(values) -1:
                        if A[i-1][j-1] == 'X':
                            count += 1
                        if A[i+1][j-1] == 'X':
                            count += 1
                    elif j == 0:
                        if A[i+1][j+1] == 'X':
                            count += 1
                        if A[i-1][j+1] == 'X':
                            count += 1
                    else:
                        if A[i+1][j+1] == 'X':
                            count += 1
                        if A[i-1][j+1] == 'X':
                            count += 1
                        if A[i-1][j-1] == 'X':
                            count += 1
                        if A[i+1][j-1] == 'X':
                            count += 1
                resultStr += str(count)
            else:
                resultStr += values[j]
        result.append(resultStr)
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

