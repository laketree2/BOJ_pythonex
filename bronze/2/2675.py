t = int(input()) #테스트케이스 입력받기
text = "" #출력할 문자열 입력받을 변수 초기화
for _ in range(t): #테스트케이스 만큼 반복
    num, alpha = list(map(input().split())) #반복할 횟수 num, 문자열alpha 입력받기
    for x in alpha:
        text = alpha[x]*num
print(text)