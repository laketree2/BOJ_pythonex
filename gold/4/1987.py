import sys
input = sys.stdin.readline

R,C = map(int, input().split()) # R은 가로를 의미, C는 세로를 의미
graph = [list(input()) for _ in range(R)] # graph는 2차원 배열로, R만큼 
set = set() # 중복값을 막기 위해 set()함수를 사용한다.
dx = [-1, 1, 0, 0] # x의 이동거리 범위를 담음
dy = [0, 0, -1, 1] # y의 이동거리 범위를 담음
answer = 0 # 최종 값을 담아둘 변수

def DFS(x, y): # DFS 함수 생성 - 0,0입력 받음
    global answer # answer 변수를 전역변수화
    for i in range(4): # 상하좌우로 움직일 수 있으므로, 4번 반복
        nx = x + dx[i] # nx은 다음 x의 좌표값을 저장
        ny = y + dy[i] # ny은 다음 y의 좌표값을 저장
        if 0 <= nx < R and 0 <= ny < C: # 다음 좌표값들이 범위를 넘어가지 않는다면,
            if graph[nx][ny] not in set: #또, set안에 그래프 값이 없다면(중복값을 제외하기 위해)
                set.add(graph[nx][ny]) # 그 값을 set안에 넣기
                DFS(nx, ny) # 그리고, 다음 값으로 넘기기
                set.discard(graph[nx][ny]) #discard는 값을 지우는 역할을 함 .remove는 없는 값을 지우면, 오류가  발생, .discard는 없는 값을 지우라해도 오류가 생기지 않음
    answer = max(answer, len(set)) # 
    return answer

set.add(graph[0][0]) #그래프의 첫 문자열을 set안에 집어넣음
DFS(0,0) # DFS함수 실행 x,y는 0부터 시작
print(answer) # 최종값 출력