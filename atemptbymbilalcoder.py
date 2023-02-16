def minesweeper(test):
    def countX(lst, rn, cn):
        def setRStart(rn):
            if rn-1 <= 0:
                return 0
            else:
                return rn-1

        def setREnd(rn):
            if rn+2 > len(lst):
                return len(lst)
            else:
                return rn + 2
            
        def setCStart(cn):
            if cn-1 <= 0:
                return 0
            else:
                return cn-1

        def setCEnd(cn):
            if cn+2 > len(lst[rn]):
                return len(lst)
            else:
                return cn + 2

        rStart = setRStart(rn)
        rEnd = setREnd(rn)
        cStart = setCStart(cn)
        cEnd = setCEnd(cn)
        count = 0

        for r in range(rStart,rEnd):
            for c in range(cStart,cEnd):
                if lst[r][c] == "X":
                    count = count + 1

        return count

    for rn, r in enumerate(test):
        test[rn] = list(test[rn])
        for cn, c in enumerate(test):
            if test[rn][cn] == "O":
                count = countX(test, rn, cn)
                test[rn][cn] = str(count)

    for i, d in enumerate(test):
        test[i] = "".join(d)
    
    return test

test = ["XOOXXXOO", 
            "OOOOXOXX", 
            "XXOXXOOO", 
            "OXOOOXXX", 
            "OOXXXXOX", 
            "XOXXXOXO", 
            "OOOXOXOX", 
            "XOXXOXOX"]

print(minesweeper(test))