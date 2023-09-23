import sys

n = int(sys.stdin.readline())
sequence = list(map(int, sys.stdin.readline().rstrip().split()))
s_list = sorted(sequence) #비내림차순 정렬

list = []
for i in range(n):
    index = s_list.index(sequence[i])
    list.append(index)
    s_list[index] -= 1
    
print(list)