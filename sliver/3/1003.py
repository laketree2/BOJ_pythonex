'''
0과 1이 나타나는 순서는 수열의 관계를 가짐
fibo(0) = 0
fibo(1) = 1
fibo(2) = fibo(0)+fibo(1) 0 + 1
fibo(3) = fibo(2) + fibo(1) + fibo(0) 0+1+1+0
'''
t = int(input())
for i in range(t):
    n = int(input())
    zero,one=1,0 #0, 1 개수 저장 변수 초기화
    for i in range(n):
        zero,one = one,zero+one #수열 규칙 -> 0의 개수와 1의 개수를 더한 n-2번째이상 피보나치의 규칙성
    print(zero,one)

'''
a = 0 / b = 1 의 등장 횟수
0과 1의 등장횟수는 고정이므로 리스트에 생성
2 이상부터는 0과 1의 반복, fibo(n) = fibo(n-1)+fibo(n-2)을 만족
일반식을 활용해 0과 1의 등장횟수에 추가
튜플의 쌍을 2차원 리스트로 보고 삽입
'''
t = int(input())
a = 0
b = 0
while(t):
    n = int(input())
    n_list = [(1,0),(0,1)]
    for i in range(2, n+1):
        a = n_list[i-1][0]+n_list[i-2][0]
        b = n_list[i-1][1]+n_list[i-2][1]
        n_list.append((a,b))
    print(n_list)
    print(*n_list[n])
    t -= 1