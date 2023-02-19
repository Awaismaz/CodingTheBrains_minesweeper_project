"""Name : Salman
    project : minesweeper project
    submission date : 19 feb
"""


def minesweeper(A):
    #code that coverts the test matrix into desired output
    input1 = input("Select the method\nPress '1' for method_1 and '2' for method_2 : ")

        #   method  #  1:
    if input1 == '1':
        print("sir check this method it has some plz correct it!\n")

        A.insert(0 , '00000000')  
        result = []
        for i,pair in enumerate(A):
            string = ''
            for j , ind in enumerate(pair):
                pass
            
                if ind == "X":
                    string += "X"
                else :
                    counter = 0
                    for x in A[i-1 : i+2]:
                        for y in x[j-1 : j+2]:
                            if y == "X":
                                counter+=1
                    string += str(counter)
            
            result.append(string)
            
        return result[1:]
    
    
    
    elif input1 == '2':

        result=[]
        row = len(A)
        coloumns = len(A[7]) # change this into how many rows you will enter as input
        
        

    # for loop for changing rows 
        for i in range(row): 
            string_result = ''

    # for loop for changing index
            for j in range(coloumns):
                if A[i][j] == 'X':

    # if index is on x then add it to the string
                    string_result += 'X'
                else:

    # if index is on o then start the counter
                    count = 0

    # for loop for 3 rows checking bomb
                    for x in range(i-1 , i+2):

    # for loop for 3 coloumns checking bomb
                        for y in range(j-1 , j+2):
                            if (x >= 0 and x < row  and y >= 0 and y < coloumns and A[x][y] == 'X'):
                                count +=1          
    # converting o's to numbers 
                    string_result += str(count)

    # now append the str to result        
            result.append(string_result)
        return result

    else:
        print("wrong input")

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


# 4 nusted loops
# then condition if x count increase or decrease