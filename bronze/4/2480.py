
'''
같은 눈이 3개가 나오면 10,000원+(같은 눈)×1,000원의 상금을 받게 된다. 
같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)×100원의 상금을 받게 된다. 
모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)×100원의 상금을 받게 된다. 
''' 
one, two, three = map(int, input().split()) #1,2,3번째 값 입력받기

def max(): #함수 정의
    if (one>=two)and(three<=one): #1번째가 최대값
        return one #최대값(1번째)반환
    if (one<=two)and(two>=three): #2번째가 최대값
        return two #최대값(2번째)반환
    if (three>=one)and(three>=two): #3번째가 최대값
        return three #최대값(3번째)반환

if one == two == three:
    print(10000+one*1000)
elif one == two:
    print(1000+one*100)
elif one == three:
    print(1000+one*100)
elif two == three:
    print(1000+two*100)
else:
    print(100 * max())