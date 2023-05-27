def minesweeper(test):
    #code that coverts the test matrix into desired output

    #creating a new list
    desired = [[0 for i in range(8)] for j in range(8)]

    #adding a layer of Os
    for i in range(len(test)):
        test[i] = 'O' + test[i] + 'O'
    test.insert(0,'OOOOOOOOOO')
    test.append('OOOOOOOOOO')

    #creating the implication code
    for i in range(1,len(test)-1):
        for j in range(1, len(test)-1):
            if test[i][j] == 'X':
                desired[i-1][j-1] = 'X'
            elif test[i][j] == 'O':
                count = 0
                if test[i-1][j-1] == 'X':
                    count += 1
                if test[i-1][j] == 'X':
                    count += 1
                if test[i-1][j+1] == 'X':
                    count += 1
                if test[i][j-1] == 'X':
                    count += 1
                if test[i][j+1] == 'X':
                    count += 1
                if test[i+1][j-1] == 'X':
                    count += 1
                if test[i+1][j] == 'X':
                    count += 1
                if test[i+1][j+1] == 'X':
                    count += 1
                desired[i-1][j-1] = count
    return desired

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

    result = (minesweeper(test))
    for i in range(len(result)):
        for j in range(len(result[i])):
            print(result[i][j],end=' ')
        print()