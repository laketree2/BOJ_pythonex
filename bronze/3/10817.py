a,b,c = map(int,input().split(' ')) #한 줄에 여러 정수형 입력받기

if(a>=b): #a와b 비교: a가 b보다 크거나 같을 때
    if(a>=c): #a와 c 비교: a가 c보다 크거나 같을 때
        if(b>=c): #b와 c비교: b가 c보다 크거나 같을 때 
            print(b) #중간값=b 출력
        else: #c가 b보다 크거나 같을 때
            print(c) #중간값=c 출력
    else:#c가 a보다 크거나 같을 때
        print(a) #중간값=a 출력
else: #b가 a보다 크거나 같은 경우
    if(b>=c): #b가 c보다 크거나 같을 때
        if(a>=c): #a가 c보다 크거나 같을 때
            print(a) #중간값=a 출력
        else: #c가 a보다 크거나 같을 때
            print(c) #중간값=c 출력
    else: #c가 b보다 크거나 같을 때
        print(b) #중간값=b 출력