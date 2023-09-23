while True: #무한반복
    a,b = map(int(input().split())) #두 정수 입력받기
    if a+b==0: #만약 같으면
        break #멈춤
    if a>b: #에이가 비보다 크면
        print("Yes") #출력
    else: #반대상황이면
        print("No") #출력