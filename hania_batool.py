def minesweeper(A):
    new = []
    for items in A:
        new.append('O' + items + 'O')
    x = map(lambda x: 'O',range(len(new[0])))
    str = ''.join(list(x))
    new.insert(0,str)
    new.append(str)    
    mines = []
    n = len(new)
    for i in range(1, n-1):
        row = ''
        col = ''
        for j in range(1, n-1):
            count = 0
            character = new[i][j]
            if(character == 'X'):
                row += 'X'
            else:
                if(character == 'O'):
                    for k in range(j-1,j+2):
                        if new[i-1][k] == 'X':
                            count += 1
                        if new[i+1][k] == 'X':
                            count += 1
                    if new[i][j-1] == 'X':
                        count += 1
                    if new[i][j+1] == 'X':
                        count += 1
                col = "{}".format(count)
                row += col
        mines.append(row)
    return mines
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
