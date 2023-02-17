def minesweeper(A):

    copy = A
    
    # Insert top & bottom padding rows
    padding = 'P' * len(A[0])
    copy.insert(0, padding)
    copy.append(padding)

    # Insert padding to each row
    for i in range(0, len(copy)):
        copy[i] = "P" + copy[i] + "P"

    #Iterate through Rows and Characters
    for row in range(1, len(copy)-1):
        for char in range(1, len(copy[0])-1):
            if copy[row][char] != 'X' and copy[row][char] != 'P':
                counter = 0

                # Checking for Mines
                for i in range(row-1, row+2):
                    for j in range(char-1,char+2):
                        if copy[i][j] == 'X':
                            counter += 1

                # Replaces 0's with count of mines
                copy[row] = copy[row][:char] + str(counter) + copy[row][char+1:]
    
    # Removes Padding
    for i in range(0, len(copy)):
        copy[i] = copy[i][1:len(copy[i])-1]

    copy.pop()
    copy.remove(padding)

    return copy

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