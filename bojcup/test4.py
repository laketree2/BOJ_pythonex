n = int(input()) #입력값
n_list = [] #좌표값
plans = [] #이동값 출력할 리스트

#시계방향 정렬
dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [1, 1, 0, -1, -1, -1, 0, 1]
#mapper = {'W':0, 'E':1, 'D':2, 'C':3, 'X':4, 'Z':5, 'A':6, 'Q':7}

#각각의 좌표 받기
for k in range(n):
    x, y = map(int, input().split())
    n_list.append([x, y])
    a = x
    b = y
    for i in range(8): #8방향에 대해서
        nx = a + dx[i][0]
        ny = b + dy[i][1]
        plans.append(nx, ny)
    x, y = nx, ny

print(n_list)