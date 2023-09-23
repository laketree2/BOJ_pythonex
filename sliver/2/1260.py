n, m, v = map(int, input().split()) #입력값 한 번에 받기
#n:정점의 개수,m:간선의 개수,v:탐색을 시작할 정점의 번호

for _ in range(n + 1):#인덱스 번호 반복문
    matrix = [[0] * (n + 1)]  # 1번째 인덱스의 번호를 0에서 1로 초기화

for i in range(m):#간선의 개수
    from_n, to_n = map(int, input().split())#DFS를 수행
    matrix[from_n][to_n] = matrix[to_n][from_n] = 1 # 간선은 양방향

visit_list = [0] * (n + 1)  # 0번 인덱스부터하면 헷갈리니까

def dfs(start_node):
    visit_list[start_node] = 1
    print(start_node, end=' ')
    for i in range(1, n + 1):
        if visit_list[i] == 0 and matrix[start_node][i] == 1:   # 아직 방문안했는데 방문해야할 곳
            dfs(i)


def bfs(start_node):
    queue = [start_node]
    visit_list[start_node] = 1
    
    while queue:
        start_node = queue.pop(0)
        print(start_node, end=' ')
        for i in range(1, n + 1):
            if visit_list[i] == 0 and matrix[start_node][i] == 1:
                queue.append(i)
                visit_list[i] = 1


dfs(v)
print()
visit_list = [0] * (n + 1)
bfs(v)


