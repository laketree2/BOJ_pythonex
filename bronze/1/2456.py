n = int(input())
n_list = [0]*3
square_n = [0]*3
for i in range(n):
    a, b, c = map(int, input().split())
    n_list[0] += a
    n_list[1] += b
    n_list[2] += c
    
    square_n[0] += a*a
    square_n[1] += b*b
    square_n[2] += c*c
    
max_value = max(n_list)
if n_list.count(max_value) == 1: #총합이 가장 큰 사람이 결정된 경우
    idx = n_list.index(max_value)
    print(idx+1, n_list[idx])
    '''
    for i in range(3): #인덱스 번호 찾기 반복문
        if n_list[i] == max_value:
            print(i+1, max_value)
    '''
else:
    m_value = max(square_n)
    idx2 = square_n.index(m_value)
    if square_n.count(m_value) == 1:
        print(idx2+1, n_list[idx2])
    else:
        print(0, n_list[idx2])