'''
tomato
토마토가 있는 곳을 기준으로 bfs 돌림
점진적으로 늘려 나감
다음으로 bfs를 돌릴 위치는 어딘가?
이미 돌린 곳은 처리되지 않도록(중복제거)
'''
from collections import deque
n, m = map(int, input().split()) #행이 줄이 된다

tomato = [list(map(int, input().split())) for _ in range(m)]#맵정보 입력받기
#방문한 곳에 대해 방문처리를 하는 변수 생성
visited = [[0]*n for _ in range(m)] #토마토의 칸과 같은 칸수 생성

dx = [-1, 1, 0, 0] #x축
dy = [0, 0, -1, 1]
now = deque()
cnt = 0

#토마토를 기준으로 bfs를 돌리기 위해 토마토 위치를 파악하기 
# 위한 순회 돌기

for i in range(m):#줄부터 순회돌기
    for j in range(n):
        if(tomato[i][j] == 1):
            now.append((i, j))
            visited[i][j] = 1 #방문처리
        elif(tomato[i][j]== -1): #못가는 곳은 1처리
            visited[i][j] = 1
            

#now bfs 토마토 값 빼주기
while(now):
    nx, ny = now.popleft() #앞에서부터 빠짐
    for i in range(4): #방향 순회
        mx = nx + dx[i]
        my = ny + dy[i]
        #인덱스 아웃 오브 레인지 처리
        if (0 <= mx < m) and (0 <= my < n) and (visited[mx][my]==0)and (visited[mx][my]!=-1):
            visited[mx][my] = visited[nx][ny] + 1 #일차 증가
            now.append((mx, my))
            
# for i in visited:
#     print(i)
# result = 0
# bp = 0
result = 0
bp = 0
for i in visited:
    for j in i:
        if(j == 0):
            result = 0
            bp = 1
            break
        result = max(result, j)
    if (bp == 1):
        break
print(result -1)