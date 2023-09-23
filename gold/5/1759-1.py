A,B = map(int, input().split())#A은 비밀번호 자리 수, B는 알파벳 수
alpha = list(input().split())#빈칸으로 암호 구분
alpha.sort()#입력받은 알파벳 정렬
answer = []
def solution(A, B):
    conso = 0
    vowel = 0
    for i in range(len(answer)):
        if (i =='a'or i=='e'or i == 'o'or i =='i'or i =='u'): # 그리고, 입력받은 answer안 문자열에 모음이 하나 있는지 판별 
            vowel +=1
        else:
            conso +=1
        if vowel >= 1 and conso >= 2:
            print(''.join(answer)) # 있다면, 출력
    def DFS():
