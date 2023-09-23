n_list = [] #입력값을 받을 빈 리스트 생성
empty_list = [] #빈 리스트 생성
for i in range(0,9): #반복
    n_list.append(int(input())) #입력값을 받아 리스트에 추가
result_list = n_list + empty_list #위치 출력을 위해 같은 리스트 추가

for i in range(0,8): #요소들 간 크기비교를 해 최대값을 마지막 인덱스 번호로 밀기
    if n_list[i]>n_list[i+1]: #값이 더 크다면
        n_list[i+1]=n_list[i] #최대값 수정
print(n_list[-1]) #마지막 인덱스 값, 최대값 출력
print(result_list.index(n_list[-1])) #최대값 번호 출력