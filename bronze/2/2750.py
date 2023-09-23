n = int(input()) #숫자들의 개수 입력받기
m = [] #n만큼 숫자를 입력받을 리스트 변수 초기화

for i in range(n): #n만큼 반복
    m.append(int(input())) #입력받기
    
for i in range(len(m)): #리스트 길이만큼 반복
    for j in range(len(m)): #오름차순 반복
        if m[i]<m[i]: #대소를 비교하여 
            m[i],m[j] = m[j],m[i] #오름차순으로 정리
for n in m: #반복문
    print(n) #출력