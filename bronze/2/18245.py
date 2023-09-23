sentence = str(input()) #문장 입력받기
line = 2 #문장을 받을 줄 입력

while string != "Was it a cat I saw?": #마지막 문장이 오기 전까지
    for i in range(0, len(sentence), line): #길이 만큼 반복
        print(sentence[i], end = '') #i번째 줄의 문장은 문장의 첫 번째 글자에서 시작해 i칸씩 건너 뛰며 읽어야함
    print()#띄어쓰기
    
    line += 1#줄 추가
    sentence = str(input()) #입력받기