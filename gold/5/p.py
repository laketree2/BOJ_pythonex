from heapq import heappop, heappush
import sys
input = sys.stdin.readline

def Dijkstra(start): #특정한 정점에 대해서 최소비용을 구하기 때문에 무조건 잡아야 함
    q = list() #힙으로 쓸 리스트 생성
    heappush(q, (0, start)) #while q를 돌기 위해 생성, 0 = cost, start = 시작점
    while q:
        dist, now = heappop(q) #값어치와 현재 정점
        distance = [float('inf')] * (n+1) #함수 안에 삽입하면 여러개 시작점에 대해 돌릴 수 있음
        if dist > distance[now]:
            continue
        for i in G[now]: #지금 보고싶은 정점에 대한 정점도착지와 간선 가중치 비용
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heappush(q, (cost, i[0]))
    return distance
n = int(input()) #정점
m = int(input()) #간선
G = [[] * (n+1) for _ in range(n+1)] #1번 노드부터
 
for _ in range(m):
    u, v, w = map(int, input().split())
    G[u].append((v, w))
    
for i in range(1, n+1):
    print(Dijkstra(i)) #모든 노드들에 대해 어느 비용이 드는지 알고 싶을 때