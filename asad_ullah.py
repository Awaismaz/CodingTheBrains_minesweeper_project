def minesweeper(A):
    #code that converts the test matrix into desired output

    length_of_list = len(A)
    result = []
    
    for j in range(length_of_list):
        length_of_string = len(A[j])
        row_result = ""
        
        for i in range(length_of_string):
            counter = 0
            for x in range(max(0, j-1), min(length_of_list, j+2)):
                for y in range(max(0, i-1), min(length_of_string, i+2)):
                    if A[x][y] == 'X':
                        counter += 1

            if A[j][i] == 'X':
                row_result += 'X'
            else:
                row_result += str(counter)
        
        result.append(row_result)

    return result

if __name__ == "__main__":
    
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
