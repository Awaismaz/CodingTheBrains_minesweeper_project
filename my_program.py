def minesweeper(A):
    rows = len(A)  # rows
    cols = len(A[0])  # cols
    B = [['0' for i in range(cols)] for j in range(rows)]

    for row in range(rows):
        for col in range(cols):
            if (A[row][col]) == "X":
                B[row][col] == "X"
            else:
                count = 0
                for r in range(max(0, row - 1), min(rows, row + 2)):
                    for c in range(max(0, col - 1), min(cols, col + 2)):
                        if A[r][c] == "X":
                            count += 1
                B[row][col] = str(count)

    return [''.join(row) for row in B]


if __name__ == "__main__":

    A = ["XOOXXXOO",
         "OOOOXOXX",
         "XXOXXOOO",
         "OXOOOXXX",
         "OOXXXXOX",
         "XOXXXOXO",
         "OOOXOXOX",
         "XOXXOXOX"]

B = minesweeper(A)  # instance
for row in B:
    print(row)

""" Minesweeper programmed by fareedcodes, Thank you!"""
