N, M = map(int, input().split())

check = [0] * (N+1)
line = 0
result = []

def combination(N, M):
    global line
    # range(N) -> 0~N-1  //  내가 원하는 것은 n ~ N-1 idx까지 들어가는 것
    if sum(check) == M:
        print(" ".join(map(str, result)))
        return
    for i in range(1, N+1):
        if check[i] == 0 and i > line:
            result.append(i)
            if i > line:
                line = i
            check[i] = 1
            combination(N, M)
            check[i] = 0
            result.pop()
            line = 0

combination(N, M)