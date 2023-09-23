import sys
input = sys.stdin.readline
print = sys.stdout.write

def find_parent(parent, x):
    if parent[x] != x: #예상한 부모 값이 아닐 때(union이 한 번 이루어 졌을 때)
        parent[x] = find_parent(parent, parent[x]) #부모 찾기 
    return parent[x]

def union_parent(parent, a, b): #제일 작은 부모 노드 통합
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a
        
n = int(input())
parent = [i for i in range(n)] #인덱스 1부터 시작, 1 무시
# info = [list(map(int, input().split())) for _ in range(n)]
s = [list(map(int, input().split())) for _ in range(n)]
info = []
for i in range(n):
    for j in range(i + 1, n):
        if s[i][j] != 0:
            info.append((s[i][j], i, j))
info.sort() #★가중치 기준으로 정렬(가중치 작은 순)

total = 0 #가중치

for i in range(len(info)): #노드의 개수가 아닌 간선의 개수
    c, a, b = info[i]

    # 사이클이 발생하지 않는 경우에만 집합에 포함(연결)
    if find_parent(parent, a) != find_parent(parent, b): #부모 노드가 다르면
        union_parent(parent, a, b) #부모 통합
        total += c

print(str(total))