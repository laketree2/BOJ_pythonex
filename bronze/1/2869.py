a, b, v = map(int,input().spilt()) #올라간a, 미끄러진 b, 높이 v 선언
day = (v-b)/(a-b) #높이에서 미끄러진 값/올라갈 수 있는 값- 미끄러진 값 : 거리 속도 시간 공식 활용
if day == int(day): #값이 정수로 나누어 떨어진다면
    print(day) #출력
else: #그렇지 않은 경우
    print(day+1) #하루를 더해 출력