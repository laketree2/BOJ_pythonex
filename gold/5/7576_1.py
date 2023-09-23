from collections import deque

N, M = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(M)]
visited = [[0] * M for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
now = deque()
for i in range(M):
    for j in range(N):
        if(tomato[i][j] == 1):
            now.append((i, j))
            visited[i][j] = 1
while(now):
    nx, ny = now.popleft()
    for i in range(4):
        mx = nx + dx[i]
        my = ny + dy[i]
        if(0 <= mx < M) and (0 <= my < N) and (visited[mx][my] == 0):
            visited[mx][my] = visited[nx][ny] + 1
            now.append((mx, my))
print(visited)
