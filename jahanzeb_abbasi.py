def minesweeper(A):

    # Insert top & bottom padding rows
    padding = 'P' * len(A[0])
    A.insert(0, padding)
    A.append(padding)

    # Insert padding to each row
    for i in range(0, len(A)):
        A[i] = "P" + A[i] + "P"

    #Iterate through Rows and Characters
    for row in range(1, len(A)-1):
        for char in range(1, len(A[0])-1):
            if A[row][char] != 'X' and A[row][char] != 'P':
                counter = 0

                # Checking for Mines
                for i in range(row-1, row+2):
                    for j in range(char-1,char+2):
                        if A[i][j] == 'X':
                            counter += 1

                # Replaces 0's with count of mines
                A[row] = A[row][:char] + str(counter) + A[row][char+1:]
    
    # Removes Padding
    for i in range(0, len(A)):
        A[i] = A[i][1:len(A[i])-1]

    A.pop()
    A.remove(padding)

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