n, s = map(int,input().split())
answer = 0
answer_list = list(map(int,input().split()))

def solution(n, s):
    global answer
    def DFS(L, sum):
        global answer
        if(L==n):
            if(sum ==s):
                answer += 1
                return
        else:
            DFS(L+1,sum+answer_list[L])
            DFS(L+1,sum)
    DFS(0,0)
    if (s==0):
        answer -=1
        return answer
print(solution(n,s))

