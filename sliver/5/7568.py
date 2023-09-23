'''
x, y의 쌍이 모두 클 때, 덩치가 크다(등수 산정)
등수 k에 대하여 다음 등수는 k+1
리스트 생성 후 학생별 x,y를 입력받아 각각의 원소로 보기(튜플)
'''
#n <= 50 --> O(N**2) 시간복잡도 알고리즘 적용 가능
n = int(input())
n_list = []
for i in range(n):
    x, y = map(int, input().split())
    n_list.append((x, y))
print(n_list)
for i in range(n):
    rank = 1
    for j in range(n):
        #if i[0] < j[0] and i[1] < j[1]: --> range(n) -> n_list 수정
        if n_list[i][0] < n_list[j][0] and n_list[i][1] < n_list[j][1]:
            rank += 1
    print(rank, end = " ")

