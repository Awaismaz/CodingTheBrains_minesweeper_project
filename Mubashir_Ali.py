def minesweeper(input):
    row=len(input)
    col=len(input[0])

    input=[list(input[elements]) for elements in range(row)]

    for M_row in range(row):
        for M_col in range(col):
            if not input[M_row][M_col] == 'X':
                counter=0
                for In_row in range(M_row-1,M_row+2):
                    for In_col in range(M_col-1,M_col+2):
                        try:
                            if not (In_row==-1 or In_col==-1) and input[In_row][In_col]=='X':
                                counter+=1
                        except:
                            pass
                    input[M_row][M_col]=str(counter)
    input=[''.join(input[elements]) for elements in range(row)]
    return input                            
            
                                       
                        

        
          

    

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

