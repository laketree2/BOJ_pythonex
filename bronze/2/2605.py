'''
1번째(0그대로, 1앞)
2번째(012, 뽑은 번호 만큼 앞)
'''

import sys

n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
list = []

for i in range(n):
    list.insert(len(list) - num[i], i + 1)
    #0그대로
    # if num[i] == 0:
    #     list.append(num[i])
    # #뽑은 순서만큼 앞으로
    # else:
    #     list.insert(num[i], i )

# for i in range(len(list)+1, 1, -1):
#     print(list[i], end = " ")
# for i in reversed(range(n)):

# for i in reversed(list):
#     print(i + 1, end=" ")
for i in list:
    print(i, end = " ")