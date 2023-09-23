'''
비트마스킹, 이진수
n의 이진수 표현에서 1의 개수가 물병의 개수와 같음
k값보다 작도록 반복문을 돌려 물병을 상점에서 사들임
'''
n, k = map(int, input().split())
result = 0

while bin(n).count('1') > k: #문자열 입력 --> 문자열 카운팅
    n += 1
    result += 1
    
print(result)