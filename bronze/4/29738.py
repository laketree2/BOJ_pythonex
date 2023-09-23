import sys
input = sys.stdin.readline

t = int(input())

for i in range(1, t+1):
    x = int(input())
    if x > 4500:
        ans = "Round 1"
    elif x > 1000:
        ans = "Round 2"
    elif x > 25:
        ans = "Round 3"
    else:
        ans = "World Finals"
    print("Case #", i, ': ', ans, sep = '')
