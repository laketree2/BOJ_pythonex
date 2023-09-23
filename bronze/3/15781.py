N, M = map(int, input().split()) #헬멧의 개수 n, 조끼의 개수m 입력받기
h = list(map(int, input().split())) #헬멧의 방어력 입력받기
a = list(map(int, input().split())) #조끼의 방어력 입력받기

max_h = 0 #헬멧 방어력 최대값 변수 초기화
max_a = 0 #조끼 방어력 최대값 변수 초기화

for i in h: #헬멧 최대값 반복문
    if i > max_h: #입력값이 설정된 최대값보다 크다면
        max_h = i #해당 값을 최대값으로 설정

for j in a: #조끼 최대값 반복문
    if j >max_a: #입력값이 설정된 최대값보다 크다면
        max_a = j #해당 값을 최대값으로 설정

print(max_h+max_a) #최대값의 합 출력

