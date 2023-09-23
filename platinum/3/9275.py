#특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    #루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

#두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
parent = [0] * (n+1) #부모 테이블 초기화

# #부모 테이블 상에서, 부모를 자기 자신으로 초기화
# for i in range(1, n+1):
#     parent[i] = i

#각 연산을 하나씩 확인
for i in range(m):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

#집합 
video = []
for i in range(1, n+1):
    video.append(i)
print(video)
    # if find_parent(parent, a) != find_parent(parent, b):
    #     union_parent(parent, a, b)
    #     if video:#영상이 켜져있다면
    #         if :#토끼라면
    #             print('YES')
    #         else:
    #             print('NO')