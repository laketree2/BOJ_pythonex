count = 0 #양수 개수 저장할 변수 초기화
data = list(map(int,input().split())) # 입력값 변수 초기화

for i in data: #입력값 전체 반복문
    if i>0: #입력값이 양수이면
        count +=1 #양수 개수 추가

print(count) #최종 양수 개수 출력
