def minesweeper(A):
    # defining intermdeiate list to add zeros on periphery of given list/grid
    imd_lst = []
    for u in range(0, 8):
        A[u] = "O"+A[u]+"O"
        imd_lst.append(A[u])
    imd_lst.append("O"*10)
    imd_lst.insert(0, "O"*10)

    # writing code for iterating on each character of each string in list/grid
    output_lst = []
    for i in range(1, 9):
        s = ""
        for j in range(1, 9):
            if imd_lst[i][j] == "X":
                s += "X"
            else:
                counter = 0
                for x in range(i-1, i+2):
                    for y in range(j-1, j+2):
                        if imd_lst[x][y] == "X":
                            counter += 1
                        else:
                            pass
                s += str(counter)
        output_lst.append(s)
    return output_lst


if __name__ == "__main__":

    test = ["XOOXXXOO",
            "OOOOXOXX",
            "XXOXXOOO",
            "OXOOOXXX",
            "OOXXXXOX",
            "XOXXXOXO",
            "OOOXOXOX",
            "XOXXOXOX"]

    print(minesweeper(test))
