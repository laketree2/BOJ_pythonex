n, m = map(int, input().split())#A은 비밀번호 자리 수, B는 알파벳 수
alpha = list(input().split())#빈칸으로 암호 구분
alpha.sort()#입력받은 알파벳 정렬

def solution(n, alpha):
    answer = []
    checked = [0 for i in range(m)]
    temp = []

    def DFS(L, count):
        if(count ==n):
            answer.append(alpha())