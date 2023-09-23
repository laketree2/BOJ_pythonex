N,M = map(int,input().split()) #N은 자연수 범위 설정, M은 중복없이 수열.


def solution(N,M): # 최종 결과값.
    def DFS(L,S): # 레벨을 의미 
        temp = []# 결과값은 전역 변수로 설정.-> 생존 시간의 차이.
        result = []
        if (L == M): # 같아야 출력, 즉 레벨과 M은 같아야함.
            print(*temp)
        else: # L과 M이 같지 않다면,
            for i in range(S,N+1):# 반복문 사용-> 1부터 N까지 반복(for문은 마지막 조건 값이 안 들어가므로, N+1까지.)
                temp.append(i)
                DFS(i,L+1)
                temp.pop()
    DFS(0,1)
solution(N,M)