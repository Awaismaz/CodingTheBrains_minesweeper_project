# def minesweeper(A):
#     #code that coverts the test matrix into desired output
#     return A
A= [
  "xooxxxoo",
  "ooooxoxx",
  "xxoxxooo",
  "oxoooxxx",
  "ooxxxxox",
  "xoxxxoxo",
  "oooxoxox",
  "xoxxoxox"]

def minesweeper(A):
  rows=len(A)
  columns=len(A[0])
  output=[ list(A[i]) for i in  range(rows)]
  for row in range(rows):
    for col in range(columns):
      if A[row][col]!="x":
        counter=0
        for k in range(max(0, row-1), min(rows, row+2)):
          for l in range(max(0, col-1), min(columns, col+2)):
            if A[k][l]=="x":  
               counter=counter+1
        output[row][col]=str(counter)
         
  return output


final_result=minesweeper(A)
for row in final_result:
  z=(" | ".join(row))
  print(z)


# if __name__=="__main__":
    
#     test = ["XOOXXXOO", 
#             "OOOOXOXX", 
#             "XXOXXOOO", 
#             "OXOOOXXX", 
#             "OOXXXXOX", 
#             "XOXXXOXO", 
#             "OOOXOXOX", 
#             "XOXXOXOX"]

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

    # print(minesweeper(test))

