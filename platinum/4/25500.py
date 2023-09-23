from heapq import heappop, heappush
import sys
input = sys.stdin.readline

def Dijkstra(start):
    q = list()
    distance = [float('inf')] * (N + 1)
    distance[start] = 0
    heappush(q, (0, start))
    while q:
        dist, now = heappop(q)
        if dist > distance[now]:
            continue
        for i in G[now].keys():
            cost = dist + G[now][i]
            if cost < distance[i]:
                distance[i] = cost
                heappush(q, (cost, i))
    return distance

N, K = map(int, input().split())
G = [dict() for _ in range(N + 1)]
hx = list()
hy = list()
hz = [0] * (N + 1)
for i in range(1, N + 1):
    x, y, z = map(int, input().split())
    hx.append((x, i))
    hy.append((y, i))
    hz[i] = z
hx.sort()
hy.sort()

for i in range(1, N):
    x1, a = hx[i]
    x2, b = hx[i - 1]
    if (hz[a] + hz[b]) % K == 0:
        G[a][b] = min(hz[a] + hz[b], x1 - x2)
        G[b][a] = min(hz[a] + hz[b], x1 - x2)
    else:
        G[a][b] = x1 - x2
        G[b][a] = x1 - x2

for i in range(1, N):
    y1, a = hy[i]
    y2, b = hy[i - 1]
    if (hz[a] + hz[b]) % K == 0:
        if b in G[a]:
            G[a][b] = min(G[a][b], hz[a] + hz[b], y1 - y2)
            G[b][a] = min(G[b][a], hz[a] + hz[b], y1 - y2)
        else:
            G[a][b] = min(hz[a] + hz[b], y1 - y2)
            G[b][a] = min(hz[a] + hz[b], y1 - y2)
    else:
        if b in G[a]:
            G[a][b] = min(G[a][b], y1 - y2)
            G[b][a] = min(G[b][a], y1 - y2)
        else:
            G[a][b] = y1 - y2
            G[b][a] = y1 - y2

for a in range(1, N + 1):
    for b in range(i + 1, N + 1):
        if (hz[a] + hz[b]) % K == 0:
            if b in G[a]:
                if G[a][b] > hz[a] + hz[b]:
                    G[a][b] = hz[a] + hz[b]
                    G[b][a] = hz[a] + hz[b]
            else:
                G[a][b] = hz[a] + hz[b]
                G[b][a] = hz[a] + hz[b]

d = Dijkstra(1)
for i in d[1 : ]:
    print(i)