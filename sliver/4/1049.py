n, m = map(int, input().split()) #기타줄을 n개사기 위해 필요한 돈의 최솟값, 각 브랜드의 패키지 가격과 낱개의 가격 입력받기

answer = 0 #최소 돈의 수를 저장할 변수 초기화
price_list = [] #지출될 수 있는 돈의 가격을 저장할 리스트 선언

for _ in range(m): #반복
    price = tuple(map(int, input().split())) #
    price_list.append(price)

bundle = sorted(price_list, key=lambda x : x[0]) #6개 패키지 가격이 제일 싼 순서대로 정렬한 리스트
single = sorted(price_list, key=lambda x : x[1]) #낱개 가격이 제일 싼 순서로 정렬한 리스트
#6개 패키지 가격이 가장 싼 물건과 낱개 가격이 가장 싼 물건의 값을 비교했을 때
if  bundle[0][0] <= single[0][1] * 6: #6개 패키지 가격이 낱개씩 6개 사는거 보다 싸거나 같다면
    answer =  bundle[0][0] * (n // 6) + single[0][1] * (n % 6) #n을 6으로 나눠 몫만큼 묶음으로 사고 나머지만큼 낱개로 구입
    if  bundle[0][0] < single[0][1] * (n % 6): #6개 패키지 자체가 더 가격이 저렴하면
        answer =  bundle[0][0] * (n//6 + 1) #패키지채로 구입
else: #패키지 자체가 낱개로 구입하는거보다 비싸다면
    answer = single[0][1] * n #전부 낱개로 구입

print(answer) #출력