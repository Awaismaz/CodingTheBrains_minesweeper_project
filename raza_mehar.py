def minesweeper(matrix):

   
    matrix.append("00000000")
    matrix.insert(0, "00000000")
    
    row = len(matrix)
    col = len(matrix[0])

    for i in range(row):
        matrix[i] = "0" + matrix[i] + "0"

    row = len(matrix)
    col = len(matrix[0])

    for i in range(1, row-1):
        
        for j in range(1, col-1):
            str1 = ""
            if matrix[i][j] == "O":
                if j > 0 and matrix[i][j-1] == "X": #Left
                        str1 += "X"
                if j < col-1 and matrix[i][j+1] == "X": #Right
                        str1 += "X"
                if i > 0 and matrix[i-1][j] == "X": #Top
                        str1 += "X"
                if i < row-1 and matrix[i+1][j] == "X": #Bottom
                        str1 += "X"
                if i > 0 and j > 0 and matrix[i-1][j-1] == "X": #Top Left
                        str1 += "X"
                if i > 0 and j < col-1 and matrix[i-1][j+1] == "X": #Top Right
                        str1 += "X"
                if i < row-1 and j > 0 and matrix[i+1][j-1] == "X": #Bottom Left
                        str1 += "X"
                if i < row-1 and j < col-1 and matrix[i+1][j+1] == "X": #Bottom Right
                        str1 += "X"
                #print("Row", i, "Col", j, "Length", len(str))
                abc = str(len(str1))
                #print(abc)
                matrix[i] = matrix[i][:j] + abc + matrix[i][j+1:]
    return matrix


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
    print('\n'.join(minesweeper(test)))

