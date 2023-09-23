n = int(input())
n_list = list(map(int, input().split()))

inc, dec = [1]*n, [1]*n

for i in range(1, n):
    if n_list <= n_list[i+1]:
        