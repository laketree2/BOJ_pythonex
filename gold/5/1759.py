A,B = map(int, input().split())#A은 비밀번호 자리 수, B는 알파벳 수
alpha = list(input().split())#빈칸으로 암호 구분
alpha.sort()#입력받은 알파벳 정렬
checked = [0 for z in range(B)]

def solution(A,B): # 입력받은 두 수, A와 B 매개 변수로 받음.
    def DFS(L,i): # L은 레벨을 의미, i는 반복문의 다음 단계로 넘어가게 도와주는 역할
        global consonant, vo 
        consonant, vo = 0, 0
        
        if L == A: #만약 L이 A와 같다면(L과 A의 길이)
            for y in range(len(answer)):
                if answer[y] in vowel: # 그리고, 입력받은 answer안 문자열에 모음이 하나 있는지 판별 
                    vo +=1
                else:
                    consonant +=1
            #모음 1개 이상, 자음 2개 이상
            if vo >= 1 and consonant >= 2:
                print(''.join(answer)) # 있다면, 출력
                
        for x in range(i,B): # 판별를 위한 반복문
            answer.append(alpha[x]) # answer에 alpha 문자열을 추가
            DFS(L+1,i+1) # 재귀함수
            answer.pop()
    DFS(0,0) #DFS 함수를 실행 시킴

answer = [] # 결과값을 담을 answer 리스트 생성
vowel = ['a','e','i','o','u']
consonant = 0 
vo = 0
solution(A,B) # solution 함수 실행