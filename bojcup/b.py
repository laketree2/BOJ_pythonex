'''
하루 지날 때마다 역량이 늘어남
기본치 n_list
늘어날 수 있는 최대 양은 그들의 기본값만큼
'''
n, m = map(int, input().split())
n_list = list(map(int, input().split())) #역량
x = 0
ability = []
num = []
#조건
for i in range(m):
    t, q = map(int, input().split()) #오름차순, t일까지 q이상
    for j in range(len(n_list)):
        if t <= n_list[j]:#각 원소의 기본값보다 작거나 같을 때
            if t != 1:  #1이면 더하지 않음
                x = n_list[j] + t
                ability.append(x) 
            else:
                x = n_list[j]
                ability.append(x)
    if sum(ability) >= q:
        num.append(sum(ability))

if not num:
    print(-1)
else:
    print(max(num))
    
'''
4 3
4 3 6 1
1 2
3 8
4 10
=>26
2 1
2 5
1 10
=>-1
'''