''' MineSweeper project By
    Ghazi Abdullah
    Date : 17 Feb 2023'''

def minesweeper(A):
    # inserting zeros all across the borders
    A.insert(0,'00000000')
    A.append('00000000')
    for i,row in enumerate(A):
        for j,col in enumerate(row):
            if j==0:
                v ='0'+A[i]+'0'
                A[i]=v
    
    # initialization
    temp=[]
    final=[]
    count=0
    end=''
    index=0

    for i,row in enumerate(A):
        final.append(end) #---> will append the strings
        end=''
        for j,col in enumerate(row):
            temp.append(col) # ----> Create a list in which all elements are separated like ['X','O','O',.....]

            if col == 'O': 
                # To find the number of Xs around O
                for k in A[i-1:i+2]:
                    for l in k[j-1:j+2]:  
                        if l=='X':
                            count+=1 #---> This will count the number of Xs
            
                temp[index]=count  # ---> Replaces O with count                                                                                                                              
                count=0
            
            if temp[index]!='0': # ---> Remove the zeros 
                end=end+str(temp[index]) # ---> Will combine the separated elements to make a string
            index+=1
    final=final[2:] # ---> Remove unnecessary zeros   
 
    return final

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
