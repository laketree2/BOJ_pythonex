t_piece = list(map(int, input().split()))#나무조각 순서 입력받기
t_order = [1, 2, 3, 4, 5]#나무조각 순서 리스트 정의

while True:#맞을 떄 까지 반복
    for i in range(len(t_piece)-1): #나무조각의 문자열 길이에서 하나 뺀 곳 까지
        if t_piece[i] > t_piece[i+1]:#인접한 두 수를 비교
            t_piece[i], t_piece[i+1] = t_piece[i+1], t_piece[i]#큰 수를 뒤로 보냄
            print(" ".join(map(str, t_piece)))#리스트에 넣어 정렬하고 출력시 띄어쓰기로 구분된 문자열로 출력
            #리스트 안 요소들이 int형이면 join을 통해 바로 합칠 수 없고, str로 형변환-->map 사용
    if t_piece == t_order:#입력값과 나무조각 순서가 같아지면
        break#멈춤