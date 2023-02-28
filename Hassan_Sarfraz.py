def checkMine(i,j,A):
    mineCount = 0
    x=i-1
    y=j-1
         
    for k in range (x,x+3,1):
        for l in range (y,y+3,1):
            if (k == i) and (l==j):
                pass
            else:
                if A[k][l]=="X":
                    mineCount= mineCount+ 1                
                else:
                    pass
                
    return mineCount

    
def firstRow(i,j,A):
    mineCount = 0
    x=i-0
    y=j-1
        
    for k in range (x,x+2,1):
        for l in range (y,y+3,1):
            if (k == i) and (l==j):
                pass
            else:
                if A[k][l]=="X":
                    mineCount= mineCount+ 1                
                else:
                    pass
                
    return mineCount
    
def firstColumn(i,j,A):
    mineCount = 0
    x=i-1
    y=j-0
        
    for k in range (x,x+3,1):
        for l in range (y,y+2,1):
            if (k == i) and (l==j):
                pass
            else:
                if A[k][l]=="X":
                    mineCount= mineCount+ 1                
                else:
                    pass
                
    return mineCount


def lastColumn(i,j,A):
    mineCount = 0
    x=i-1
    y=j-1
        
    for k in range (x,x+3,1):
        for l in range (y,y+2,1):
            if (k == i) and (l==j):
                pass
            else:
                if A[k][l]=="X":
                    mineCount= mineCount+ 1                
                else:
                    pass
                
    return mineCount

    
def lastRow(i,j,A):
    mineCount = 0
    x=i-1
    y=j-1
        
    for k in range (x,x+2,1):
        for l in range (y,y+3,1):
            if (k == i) and (l==j):
                pass
            else:
                if A[k][l]=="X":
                    mineCount= mineCount+ 1                
                else:
                    pass
                
    return mineCount




def minesweeper(A):
    
    length =len(A)-1
    
    B=[]
    
    for i in range (length+1):
        mineString=""

        for j in range (length+1):
            mineCount = 0

            #for all "X" that are present
            if A[i][j]=="X":
                mineString=mineString+"X"
        
            #for top left corner
            elif i==0 and j== 0:
                if(A[0][1]=="X"):
                    mineCount =mineCount +1
                if(A[1][0]=="X"):
                    mineCount =mineCount +1
                if(A[1][1]=="X"):
                    mineCount =mineCount +1
                   
                mineString=mineString+str(mineCount)
                
            #for top right corner   
            elif i==0 and j== length:
                if(A[0][j-1]=="X"):
                    mineCount =mineCount +1
                if(A[1][j]):
                    mineCount =mineCount +1
                if(A[1][j-1]):
                    mineCount =mineCount +1
                   
                mineString=mineString+str(mineCount)

            #for first row
            elif i==0 and j!=length:
                mineCount=( firstRow(i,j,A))
                mineString=mineString+str(mineCount)

                      
            #for first column
            elif j==0 and i!=length:
                mineCount=( firstColumn(i,j,A))
                mineString=mineString+str(mineCount)

                
            #for last column
            elif j ==length and i !=length:
                mineCount=lastColumn(i,j,A)
                mineString=mineString+str(mineCount)
            
            #for all in between             
            elif i!=length and i!=0 and j!=length and j!=0:                
                mineCount=(checkMine(i,j,A))   
                mineString=mineString+str(mineCount)
            
            #for bottom left corner
            elif j==0 and i == length :
                if(A[length-1][j]=="X"):
                    mineCount =mineCount +1
                if(A[length-1][j+1]):
                    mineCount =mineCount +1
                if(A[length][j+1]):
                    mineCount =mineCount +1           
                mineString=mineString+str(mineCount)
                
                
            #for bottom right corner
            elif j==length and i == length :
                if(A[length-1][j]=="X"):
                    mineCount =mineCount +1
                if(A[length-1][j-1]):
                    mineCount =mineCount +1
                if(A[length][j-1]):
                    mineCount =mineCount +1                    
                mineString=mineString+str(mineCount)
                
            #for last row
            elif i==length:
                    mineCount=(lastRow(i,j,A))   
                    mineString=mineString+str(mineCount)

        B.append(mineString)
                        

            
                   
    #code that coverts the test matrix into desired output
    A=B
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

