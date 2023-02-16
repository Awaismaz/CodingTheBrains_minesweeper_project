def minesweeper(a):
    # Find the number of rows and columns in the input list
    rows = len(a)
    cols = len(a[0])
    # Initialize an empty list to store the output
    output = []
    
    for i in range(rows):
        row_output = ""
        for j in range(cols):
            if a[i][j] == "X":
                row_output += "X"
            else:
                count = 0
                # Loop through each neighbor cell using two nested loops
                for x in range(i-1, i+2):
                    for y in range(j-1, j+2):
                        # Check if the neighbor cell is within the input list and contains a mine
                        if (x >= 0 and x < rows and y >= 0 and y < cols and a[x][y] == "X"):
                            count += 1
                # Add the count of mines to the row_output string
                row_output += str(count)
        # Add the row_output string to the output list
        output.append(row_output)
        
    return output

if __name__=="__main__":
    test = ["XOOXXXOO", 
            "OOOOXOXX", 
            "XXOXXOOO", 
            "OXOOOXXX", 
            "OOXXXXOX", 
            "XOXXXOXO", 
            "OOOXOXOX", 
            "XOXXOXOX"]
    
    output = minesweeper(test)
    print(output)
 
