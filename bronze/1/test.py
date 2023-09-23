```py
from collections import deque

R, C = map(int, input().split())
S = list() #호수 그림 받는거
V = [[0 for _ in range(C)] for _ in range(R)] #visited list 방문 안했으면 0 했으면 1
X = deque() #모든 X의 인덱스 저장
next_X = deque() #이따 알아서 이해할 친구임
melt = deque() #얘도 ㅇㅇ
L = 0 #하나의 L의 인덱스 값 저장할 변수
for i in range(R):
    tmp = list(input())
    for j in range(C):
        if(tmp[j] == 'X'):
            next_X.append((i, j))
        if(L != 0):
            pass
        elif(tmp[j] == 'L'):
            L = (i, j)
    S.append(tmp) #반복문이 돌아가며 S에 줄대로 입력받고 동시에 L과 X들의 인덱스 저장

S[L[0]][L[1]] = '.'
V[L[0]][L[1]] = 1
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
p = 0 #breakpoint
cnt = 0
now = deque()
now.append(L)

while(cnt < 10):
    while(melt):
        nx, ny = melt.popleft()
        S[nx][ny] = '.'

    while(now): #여기 반복문은 그냥 BFS랍니다 기준으로 잡은 L의 호수 전체 탐색
        nx, ny = now.popleft()
        if(S[nx][ny] == 'L'): #다른 L에 도착하면 코드 종료
            p = 1
            break
        S[nx][ny] = '.'
        V[nx][ny] = 1
        for i in range(4):
            mx = nx + dx[i]
            my = ny + dy[i]
            if(0 <= mx < R) and (0 <= my < C) and ((S[mx][my] == '.') or (S[mx][my] == 'L')) and (V[mx][my] == 0):
                V[mx][my] = 1
                now.append((mx, my))

    if(p == 1): #다른 L에 도착하면 코드 종료
        print(cnt)
        break
    cnt += 1

    X = deque(next_X)
    next_X.clear()

    while(X): #X의 인덱스로 BFS를 돌릴건데
        check = 0
        nx, ny = X.popleft()
        for i in range(4):
            mx = nx + dx[i]
            my = ny + dy[i]
            if(0 <= mx < R) and (0 <= my < C) and ((S[mx][my] == '.') or (S[mx][my] == 'L')):
                check = 1
                if(V[mx][my] == 1): #만약에 그게 이미 방문한 곳 옆에 붙어있던 X면
                    now.append((nx, ny)) #걔는 그 다음에 방문할 인덱스기 때문에 now에 append
                else:
                    melt.append((nx, ny)) #아니면 그냥 녹을 애라서 melt에 append
        if(check == 0):
            next_X.append((nx, ny)) #사방에 X로 둘러쌓여있다? 그럼 다음에도 X에서 돌아갈 친구다~ 
```