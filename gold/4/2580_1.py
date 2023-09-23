def row(a, n): # 가로
    for i in range(16):
        if n == sudoku[a][i]: # 이미 있으면
            return False
    return True

def column(a, n): # 세로
    for i in range(16):
        if n == sudoku[i][a]: # 이미 있으면
            return False
    return True

def square(y, x, n): # 3x3 칸
    for i in range(4):
        for j in range(4):
            if n == sudoku[y//4 * 4 + i][x//4 * 4 + j]: # 칸내에 이미 있으면
                return False
    return True

def find(n):
    if n == len(blank): # 빈 공간 만큼 사용했으면
        for i in sudoku: # 출력 후
            print(*i) 
        exit() # 강제 종료

    for i in range(1,101):
        y = blank[n][0]
        x = blank[n][1]
        if column(x,i) and row(y,i) and square(y, x, i):
            sudoku[y][x] = i
            find(n+1)
            sudoku[y][x] = 0

import sys
sudoku = [list(map(int,sys.stdin.readline().split())) for _ in range(16)]
blank = []
for i in range(16):
    for j in range(16):
        if sudoku[i][j] == 0:
            blank.append([i,j])
print("answer")
print(find(0))