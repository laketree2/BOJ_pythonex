n =list(map(int,input().split())) #입력값 받기
print(sorted(n))
if n == sorted(n):
    print("ascending")
elif n == sorted(reverse=True):
    print("desending")
else:
    print("mixing")