from collections import deque
import sys
input = sys.stdin.readline


n, m = map(int, input().split())
dead = [list(map(int, input().split()))for _ in range(n)]
visited = [[0]for _ in range(n)]
# for i in range(n):
#     dead.append(list(map(int, input().split())))
dx = [-1, 1, 0, 0] #x축
dy = [0, 0, -1, 1]
now = deque()

h = int(input())
cnt = 0

for i in range(m):
    for j in range(n):
        if(dead[i][j] > h):
            now.append((i, j))
            visited[i][j] = 1
        elif(dead[i][j] == -1):
            visited[i][j] = 1

# for i in range(m):#줄부터 순회돌기
#     for j in range(n):
#         if(tomato[i][j] == 1):
#             now.append((i, j))
#             visited[i][j] = 1 #방문처리
#         elif(tomato[i][j]== -1): #못가는 곳은 1처리
#             visited[i][j] = 1

while(now):
    nx, ny = now.popleft() #앞에서부터 빠짐
    for i in range(4): #방향 순회
        mx = nx + dx[i]
        my = ny + dy[i]
        #인덱스 아웃 오브 레인지 처리
        if (0 <= mx < m) and (0 <= my < n) and (visited[mx][my]==0)and (visited[mx][my]!=-1):
            visited[mx][my] = visited[nx][ny] + 1 #일차 증가
            now.append((mx, my))

for i in visited:
    for j in i:
        if(j == dead[n][m]):
            result = 0
            bp = 1
            break
        result = max(result, j)
    if (bp == 1):
        break
print(result -1)