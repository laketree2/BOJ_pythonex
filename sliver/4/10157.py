'''
시계방향으로 돌아가면서 배치(위로 끝까지, 오른쪽으로 끝까지,, dfs)
좌석번호 x, y를 출력
좌석 배정하지 못하는 경우 0

달팽이 수열? 활용 방법을 모르겠음
r, c 반복, 모서리 기준 i 2번에 1씩 증가

'''

c, r = map(int, input().split())
k = int(input())

#시계방향
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
x, y = 0

#맵 정보 입력받기
arr = [[0]*c for _ in range(r)] #좌표형식으로 저장?
visited = [[0]*c for _ in range(r)]

if k > c*r:
    print(0)
else:
    dfs(k)

def dfs(k):
    if arr[x][y] == 0:
        arr[x][y] = 1
        dfs(k)
        
    if x<= -1 or x >= c or y <= -1 or y >= r: #범위 이탈시
        #방향 틀기

for i in range(r):
    for j in range(c):
        
