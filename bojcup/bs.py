a, b = map(int, input().split()) #최소, 최대
k, x = map(int, input().split()) #브실, 플마

cnt = 0

for i in range(k-x, k+x+1):
    if a<=i<=b:
        cnt += 1

if cnt != 0:
    print(cnt)
else:
    print("IMPOSSIBLE")