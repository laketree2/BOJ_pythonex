s, n, m = map(int, input().split())
x = 0 #사용 여부
for i in range(n+m):
    b = int(input())
    if b == 1:
        if s != x:
            x += 1
        else:
            s *= 2
            x += 1
    elif b == 0:
        x -= 1

print(s)

