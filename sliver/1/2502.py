import sys
input = sys.stdin.readline

d, k = map(int, input().split())

a, b = 1, 1 
for _ in range(4, d + 1):
    a, b = b, a + b

one = 1
two = 0
while True:
    tmp = k - a * one
    if tmp < 0:
        break

    if tmp % b == 0:
        two = tmp // b
        break

    one += 1

print(one)
print(two)