def solve(sudoku):
    out = sudoku

    def check(num, l, c):
        possible = True
        for pos in out[l]:
            if pos == num:
                possible = False
        for line in out:
            if line[c] == num:
                possible = False
        
        if possible:
            out[l][c] = num

    for line in range(len(out)):
        for coll in range(len(line)):
            if out[line][coll] == 0:
                for i in range(1, 10):
                    if not check(i, line, coll):
                        out[line][coll] = i
                        break
                    elif i == 9:
                        continue
            else:
                continue


example1 = [[0, 1, 0, 0],
            [0, 0, 0, 4],
            [3, 0, 2, 0],
            [0, 0, 0, 0]]

example2 = [[0, 0, 9, 0, 0, 2, 0, 0, 5],
            [5, 3, 8, 0, 6, 4, 0, 0, 9],
            [1, 6, 2, 0, 0, 0, 0, 3, 0],
            [0, 0, 3, 0, 2, 7, 0, 0, 0],
            [0, 5, 4, 6, 0, 0, 1, 0, 0],
            [0, 0, 7, 0, 1, 5, 3, 4, 0],
            [3, 0, 0, 8, 0, 1, 9, 0, 6],
            [7, 0, 0, 3, 0, 0, 8, 5, 0]
            [0, 9, 1, 0, 0, 0, 4, 7, 0]]