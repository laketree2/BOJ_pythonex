s = input() #단어 입력받기
alpha='abcdefghijklmonpqrstuvwxyz' #알파벳 문자열 초기화
dic={} #딕셔너리 초기화
for i in range(len(s)) #입력받은 길이 동안
    if s[i] not in dic.keys(): #알파벳 딕셔너리 key값에 없으면
        dic[s[i]]=i#추가
for i in alpha:#반복
    if(i in s):#포함되면
        print(str(dic[i]),end=" ") #출력
    else:#없으면
        print("-1",end=" ")#출력
