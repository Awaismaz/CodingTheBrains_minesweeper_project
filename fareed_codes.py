def minesweeper(A):
    rows = len(A)  # rows are 8
    # columns of the first element are 8 digits you can take any element/index
    cols = len(A[0])
    A = [list(A[i]) for i in range(rows)]  # to create a list of strings
    # for i in range(rows):
    # x = list(A[i])
    # B.append(x)
    for i in range(rows):
        for j in range(cols):
            if not A[i][j] == "X":
                counter = 0
                for k in range(i-1, i+2):  # index's prev value
                    for l in range(j-1, j+2):
                        try:
                            if not (k == -1 or l == -1) and (A[k][l] == "X"):
                                counter += 1
                        except:
                            pass
                A[i][j] = str(counter)

    A = [''.join(A[i]) for i in range(rows)]  # to create strings from the list

    return A


if __name__ == '__main__':

    A = ["XOOXXXOO",
         "OOOOXOXX",
         "XXOXXOOO",
         "OXOOOXXX",
         "OOXXXXOX",
         "XOXXXOXO",
         "OOOXOXOX",
         "XOXXOXOX"]

print(minesweeper(A))
# B = minesweeper(A)
# for row in B:
#     print(row)
