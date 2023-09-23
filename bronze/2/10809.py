s = input() #단어 입력받기
alpha = [-1]*26 #알파벳의 수 만큼 리스트 생성

for i in range(len(s)): #단어 길이 만큼 반복
    if alpha[ord(s[i]) - 97] != -1: #없으면
        continue #계속
    else: #있으면
        alpha[ord(s[i]) - 97] = i #위치 계산

for i in alpha: #반복
    print(i, end = ' ') #출력