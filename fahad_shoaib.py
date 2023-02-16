
def minesweeper(A):
    #code that coverts the test matrix into desired output

    import numpy as np
    
    # Creating a matrix from the input to easily iterate over the characters.
    matrix = []
    for i in A:
        matrix.append(list(i))
    

    # Pad the matrix list with an extra layer of characters on each side, using the np.pad function.
    # This will make it easier to count the number of adjacent mines for each element.
    padded_matrix = np.pad(matrix, pad_width=1, constant_values='1')


    # Iterate through each element in the padded_matrix list.
    for i in range(len(padded_matrix)):
        for j in range(len(padded_matrix)):
            # Initialize a counter variable to keep track of the number of adjacent mines.
            counter = 0

            # If the current element is not a mine or a number (i.e. it is a blank space), count the number of adjacent mines.
            if (padded_matrix[i][j] != 'X') and (padded_matrix[i][j] != '1') :

                if padded_matrix[i][j+1] == 'X':
                    counter += 1
                if padded_matrix[i+1][j+1] == 'X':
                    counter += 1
                if padded_matrix[i+1][j] == 'X':
                    counter += 1
                if padded_matrix[i+1][j-1] == 'X':
                    counter += 1
                if padded_matrix[i][j-1] == 'X':
                    counter += 1
                if padded_matrix[i-1][j-1] == 'X':
                    counter += 1
                if padded_matrix[i-1][j] == 'X':
                    counter += 1
                if padded_matrix[i-1][j+1] == 'X':
                    counter += 1

                # Convert the counter value to a string as the padded_matrix is a numpy array 
                # and data types of elements in numpy array is the same.
                padded_matrix[i][j] = str(counter)


    mines_matrix = []

    # Remove the padding from the padded_matrix list, and iterate through each row.
    matrix = padded_matrix[1:-1, 1:-1]
    for i in range(len(matrix)):
        mines_string = ""
        for j in range(len(matrix)):
            mines_string += matrix[i][j]
            if j == 8:
                mines_matrix.append(mines_string)
                break

        mines_matrix.append(mines_string)
    
    return mines_matrix


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

    Desired_Output = ["X11XXX32", 
                      "3335X5XX", 
                      "XX3XX554", 
                      "3X556XXX", 
                      "24XXXX6X", 
                      "X3XXX5X3", 
                      "245X6X5X", 
                      "X2XX4X4X"]

    print(output == Desired_Output)
    