'''
주어지는 식에 임의로 괄호를 만들어 최소값 출력
-부호가 나오면 다음 -부호가 나오기 전까지 모두 괄호 안으로 묶는다.
더한 값을 하나의 값으로 보고 최소값을 만들어야 하므로 뺄셈 연산만 취급한다.
'''
input_v = input().split("-")#최소값을 위해 뺄셈 연산만 취급, -부호를 기준으로 문자열 나누기

for i in range(len(input_v)):#입력값에 대한 반복문
    input_v[i] = input_v[i].split("+")#+부호를 기준으로 나눔=값 더하기

plus_v = 0#더한 값(+),최종값 변수 초기화
#-부호가 나오기 전까지 오는 숫자는 모두 +로 이루어져 있으므로 양수
for i in range(len(input_v[0])):#입력값에 대해 반복
    plus_v += int(input_v[0][i])#덧셈 인덱스를 변수에 넣어주기 

for i in range(1, len(input_v)):#1부터 입력값까지 반복 
    minus_v = 0 #차(-)계산 변수 초기화
    for j in range(len(input_v[i])):#입력값까지 반복
        minus_v += int(input_v[i][j])#뺄셈처리

    plus_v -= minus_v #초기값(+)에서 차(-) 계산

print(plus_v)#최종값 출력