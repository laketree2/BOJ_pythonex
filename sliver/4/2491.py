'''
가장 긴 구간 출력
length++하기엔 다음으로 늘릴 때 중복 발생 
-->통과 분기점 생성
dp?
'''
n = int(input())
n_list = list(map(int, input().split()))
length = 1

if n_list[0] <= n_list[1]:
    for i in range(1, n-1):
        if n_list[i] <= n_list[i+1]:
            length += 1
            print("inc", length)
            if n_list[i] > n_list[i+1]:
                break
else:
    for i in range(1, n-1):
        if n_list[i] >= n_list[i+1]:
            length += 1
            print("dec", length)
            if n_list[i] < n_list[i+1]:
                break

print(length+1)