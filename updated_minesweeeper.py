def minesweeper(A):
    rows = len(A)
    cols = len(A[0])
    A = [list(A[a] for a in range(rows))]
    return A
if  __name__=='__main__':

    test = ["XOOXXXOO", 
            "OOOOXOXX", 
            "XXOXXOOO", 
            "OXOOOXXX", 
            "OOXXXXOX", 
            "XOXXXOXO", 
            "OOOXOXOX", 
            "XOXXOXOX"]

    print(minesweeper(test))
