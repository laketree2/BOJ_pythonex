a, b = [], [] #행렬 받을 리스트 생성
n, m = map(int,input().split()) #행렬 크기 입력받기

#행렬 원소 입력받기
for row in range(n): #한 행씩 입력 -> 행 크기만큼 반복
    #맵 객체는 이터레이터기 때문에 다대다 관계에서 list생랼 가능
    #일대다 관계에서 list를 통해 값을 확인할 수 있음
    row = list(map(input().split())) #가로 행 입력받기
    a.append(row) #입력받은 행 행렬에 삽입

for row in range(m): #반복
    row = list(map(input().split())) #행에 있는 요소값들 입력받기
    b.append(m) #추가
    
for row in range(n): #행반복
    for col in range(m): #열반복
        print(a[row][col]+b[row][col],end=" ")#행렬 a,b를 더한 행렬을 출력
    print()#줄바꿈