N = int(input())
num = list(map(int, input().split()))
cnt = 1
big = 1
small = 1
for i in range(1, N):
    if(num[i - 1] < num[i]):
        big += 1
        small = 1
        
    elif(num[i - 1] > num[i]):
        small += 1
        big = 1
        
    else:
        big += 1
        small += 1
        
    cnt = max(cnt, big, small)
print(cnt)