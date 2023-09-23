def sosu(): #함수 정의
    s_list = [False, False] + [True] * 10000 #입력값 10000, 0&1번 f. 나머지 t --> 길이 10002리스트 생성
    
    for i in range(2, 101): #입력값==10000, 101보다 작은 소수들의 배수 활용
        if s_list[i] == True: #0,1 이외 값이 들어올 경우
            for j in range(i + i, 10001, i): #i+i부터 10001,i step을 가진 반복문
                s_list[j] = False #101보다 작은 소수 f처리 --> 소수만 남음

    T = int(input()) #테스트 케이스 입력값 받기
    for _ in range(T): #테스트 케이스 동안
        n = int(input()) #짝수 입력받기

        A = n // 2 #입력 값의 중간 값으로 설정
        B = A #위와 동일
        
        for _ in range(10000): #입력값 최대 10000까지 반복
            if s_list[A] and s_list[B]: #두 값 모두 소수 리스트에 해당될경우
                print(A, B) #출력
                break #무한루프 방지
            A -= 1 #소수가 아닐 경우 탐색
            B += 1 #위와 동일

sosu()