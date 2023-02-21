def count_mines(grid, row, col):
  # initialize the counter
  count = 0
  # get the number of rows and columns in the grid
  rows = len(grid)
  cols = len(grid[0])
  # loop through the eight possible neighbors of the cell
  for i in range(-1, 2):
    for j in range(-1, 2):
      # skip the cell itself
      if i == 0 and j == 0:
        continue
      # check if the neighbor is within the grid boundaries
      if 0 <= row + i < rows and 0 <= col + j < cols:
        # check if the neighbor is a mine
        if grid[row + i][col + j] == "X":
          # increment the counter
          count += 1
  # return the counter to minesweeper function
  return count


def minesweeper(grid):
    #get rows in the grid
    row = len(grid)
    #get coloumns in the gird
    col = len(grid[0])
    #convert reach row into a list for better manipulation
    grid= [list(grid[i])  for i in range(row)]
    # loop through each cell in the grid
    for i in range(len(grid)):
        for j in range(len(grid[i])):
        # check if the cell is not a mine
            if grid[i][j] != "X":
            # replace the cell with the number of adjacent mines
                grid[i][j] = str(count_mines(grid, i, j))
    #convert list back to a string            
    grid = ["".join(grid[i])  for i in range(row)]
    #return the result to main function 
    return grid

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