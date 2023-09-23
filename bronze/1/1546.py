n = int(input())#과목 수 입력받기
t_list = list(map(int,input().split())) #입력받기
max_score = max(t_list) #최대값 할당
new_list = [] #새로운 점수를 생성할 리스트 생성
for score in t_list: #입력받은 리스트 안에 점수가 있다면
    new_list.append(score/max_score*100) #새로운 점수 생성
test_avg = sum(t_list)/n #평균 계산
print(test_avg) #출력ㄴ