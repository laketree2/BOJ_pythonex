x, y = map(int, input().split())#X월Y일 
#2007년 기준
month_31 = [1, 3, 5, 7, 8, 10, 12]#31일까지 있는 달
month_30 = [4, 6, 9, 11]#30일까지 있는 달
month_28 = [2]#2월

day = 0#요일을 판별할 변수 초기화
for i in range(1, x):#입력받은 월로 일수 판별
    if i in month_31:#31일인 달이라면
        day += 31#31일 추가
    elif i in month_30:#30일인 달이라면
        day += 30#30일 추가
    elif i in month_28:#2월이라면
        day += 28#28일 추가

day += y # 요일에 일수 추가

if day % 7 == 1: #1월1일이 월요일
    #(일주일순환)
    #7로 나누었을 때 1이 남으면 월요일
    print("MON")#요일 출력
elif day % 7 == 2: #2가 남으면 화요일
    print("TUE")#요일 출력
elif day % 7 == 3:#3이 남으면 수요일
    print("WED")#요일 출력
elif day % 7 == 4:#4가 남으면 목요일
    print("THU")#요일 출력
elif day % 7 == 5:#5가 남으면 금요일
    print("FRI")#요일출력
elif day % 7 == 6:#6이 남으면 토요일
    print("SAT")#요일출력
elif day % 7 == 0:#나누어 떨어지면 일요일
    print("SUN")#요일 출력