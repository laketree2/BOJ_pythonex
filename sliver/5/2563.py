'''
이차원 배열 보듯이
0으로 채운 후 좌표만큼의 범위 내에서 칸을 채워줌
전체 도화지의 넓이, 1개수 출력
'''

arr = [[0 for i in range(101)] for i in range(101)]
n = int(input())

for i in range(n):
    x, y = list(map(int, input().split()))
    
    for r in range(x, x+10):
        for c in range(y, y+10):
            arr[r][c] = 1
            
result = 0

for i in arr:
    result += i.count(1)
print(result)