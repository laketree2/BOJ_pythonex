import sys
input = sys.stdin.readline

y, m, d = map(int, input().split("-"))
n = int(input())

d += n
while d > 30:
    d -= 30
    m += 1
while m > 12:
    m -= 12
    y += 1

print(str(y)+"-"+str(m).zfill(2)+"-"+str(d).zfill(2))