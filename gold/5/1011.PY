import sys
import math

T = int(input()) #테스트 케이스 입력받기

for _ in range(T):
    x, y = map(int, sys.stdin.readline().rstrip().split()) #정보 입력받기
    distance = y - x #거리
    count = 0 #이동 횟수

    num = math.floor(math.sqrt(distance))   # n제곱 <= 거리 < (n+1)제곱일때 n제곱
    # num_square = num ** 2   # n제곱의 제곱(이상적 최솟값을 가지는 거리값)
    num_square = math.floor(math.pow(num, 2))
    increase_num = math.sqrt(num_square) 
    # 최소 이동 횟수가 늘어나는 기점이 되는 제곱근인 수 
    # = num_square의 제곱근

    if distance > num_square + increase_num: #거리 > 제곱수 + 증가 지점의 제곱근
        count = 2 * num + 1
    #거리 > 제곱근 and 거리 <= 제곱수 + 증가 지점 제곱근
    elif distance > num_square and distance <= num_square + increase_num:
        count = 2 * num
    elif distance == num_square: #제곱수
        count = 2 * num - 1

    if distance < 4: #예외 처리
        count = distance

    print(count)