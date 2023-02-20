def minesweeper(A):

    #code that coverts the test matrix into desired output
    rows = len(test)
    cols = len(test[0])
    my_list = []

    for i in range(rows):
        rows = ''
        for j in range(cols):
            if A[i][j] == 'X':
                rows = rows + 'X'
            else:
                counter = 0
                for i in range(max(0 ,i-1), min(rows, i+2)):
                    for j in range(max(0,j-1), min(cols, j+2)):
                        if A[i][j] == 'X':
                            counter = counter + 1
                my_list = my_list + str(counter)
        my_list.appened(rows)

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
