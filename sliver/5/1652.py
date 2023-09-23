n = int(input()) #방의 크기 입력받기
room =[] #자리 리스트 입력받기
for _ in range(n): #반복
    room.append(list(map(str,input()))) #좌석현황 입력받기
    
counting = [0,0] #가로 세로 자리 개수 담을 리스트 변수 생성
for i in range(n): #반복
    height, width = 0,0 #가로 세로 누울 수 있는 자리 변수 초기화
    for j in range(n): #반복
        if room[i][j] == ".": #입력값에 따라
            height +=1 #추가
        elif room[i][j] =="X": #벽을 만나면
            if height>=2: #좌석이 2개 이상이면
                counting[0] +=1 #누울 자리 1개로 카운팅
            height = 0 #초기화
        if room[j][i] == ".": #누울 수 있는 자리면
            width +=1 #추가
        elif room[j][i] =="X": #벽을 만날때
            if width>=2: #누울 수 있는 자리 2개 이상이면
                counting[1] +=1 #추가
            width = 0 #초기화 
            
        if j == n-1: #방의 마지막에서
            if height >=2: #누울 자리면
                counting[0] +=1 #추가
            if width >=2: #누울 자리면
                counting[1] +=1 #추가
              
print(" ".join(map(str,counting))) #출력