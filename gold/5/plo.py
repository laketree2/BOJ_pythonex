#플로이드워셜, 플로이드(O(n^3))
n = int(input())
m = int(input())
G = [[float('inf')] * (n+1) for _ in range(n+1)]
for i in range(n+1):
    G[i][i] = 0 #자기 자신
for _ in range(m):
    a, b, c = map(int, input().split())
    G[a][b] = min(G[a][b], c)#a에서 b가는 가중치값

#3중 반복문
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            G[i][j] = min(G[i][j], G[i][k] + G[k][j])

for i in range(1, n+1):
    #쥐 값을 순회하면서
    for i in range(1, n+1):
        if G[i][j] == float('inf'):
            G[i][j] = 0 #갈 수 없으면 0출력(문제조건)
for i in G[1:]:
    print(*i[1:])