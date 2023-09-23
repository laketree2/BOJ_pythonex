import sys

def dice():
    n = int(sys.stdin.readline())
    result = []
    for i in range(n):
        a, b, c = map(int, sys.stdin.readline().split())
        if(a==b==c):
            result.append(10000+a*1000)
        elif(a==b or a==c):
            result.append(1000+a*100)
        elif(b==c):
            result.append(1000+b*100)
        else:
            result.append(100*max(a,b,c))
    print(max(result))
