n, m = map(int, input().split())
t, s = map(int, input().split())

if n % 8 == 0:
    home = n +(((n//8)-1)*s)
    dok = m+((m//8)*s)+((m//8)*t)
else:
    home = n +((n//8)*s)
    dok = m+((m//8)*s)+((m//8)*t)

if home > dok:
    print("Dok")
else:
    print("Zip")
print(min(home, dok))