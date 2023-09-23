a, b = map(int, input().split())
q, r = divmod(a, b)
if a == q*b + r:
    if(0<=r<abs(b)):
        print(q)
        print(r)

    else:
        print(q+1)
        print(r-b)
