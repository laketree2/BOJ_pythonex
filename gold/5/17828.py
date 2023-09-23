import sys

n, x = map(int, sys.stdin.readline().split())

key = []
value = []

for i in range(26):
    key.append(chr(90 - i))
    value.append(26 - i)

answer_list = []

if (26 * n) < x or n > x:
    answer_list.append("!")
else:
    for i in range(len(value)):
        if x // value[i] > 0 and x % value[i] >= n - (len(answer_list) + x // value[i]):
            for j in range(x // value[i]):
                answer_list.append(key[i])
            x %= value[i]
    
    answer_list.sort()

answer = "".join(map(str, answer_list))

print(answer)