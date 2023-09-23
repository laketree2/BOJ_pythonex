N,M = map(int,input().split()) #N은 자연수 범위 설정, M은 중복없이 수열.

check = [0 for i in range(N+1)] #리스트는 1부터 시작이 아니라, 0부터 시작, 즉 N값이 포함이 안됨-> 포함하기 위해선, N+1을 해줘야함.
temp = []# 결과값은 전역 변수로 설정.-> 생존 시간의 차이.
answer = []
def solution(N,M): # 최종 결과값.
    def DFS(L): # 레벨을 의미 
        if (L == M): # 같아야 출력, 즉 레벨과 M은 같아야함.
            for n in range(M):
                print(temp[n],end=' ')
            print()
            return
        else: # L과 M이 같지 않다면,
            for i in range(1,N+1):# 반복문 사용-> 1부터 N까지 반복(for문은 마지막 조건 값이 안 들어가므로, N+1까지.)
                if check[i] == 0: #1 단계로 들어가기 위해 조건문 설정.
                    check[L] = i
                    DFS(L+1)
    DFS(0)
solution(N,M)
            