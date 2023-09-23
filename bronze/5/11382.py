a,b,c = map(int,input().split()) #입력받기
list_sum = [] #입력받은 문자열을 저장할 빈 리스트 선언
list_sum.append(a) #값 집어넣기
list_sum.append(b) #값 집어넣기
list_sum.append(c) #값 집어넣기
int_list = list(map(int,list_sum)) #리스트 안 문자열 숫자로 변환
sum = 0 #총 합 더할 변수 선언
for i in range(0,3): #반복
    sum = sum + int_list[i] #요소 더하기
print(sum) #출력