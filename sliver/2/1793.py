n = int(input())

dp = [0]*1001
dp[0] = 1 #아무것도 하지 않는 것이 1
dp[1] = 1
dp[2] = 3

while True:
    try:
        for i in range(3, n+1):
            dp[i] = (dp[i-1]+dp[i-2])
        print(dp[n])
    except:
        break

