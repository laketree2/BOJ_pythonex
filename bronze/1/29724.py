n = int(input())
apple = 4000 #가격

amass = 0
bmass = 0
cnt = 0
for i in range(n):
    t, w, h, l = map(str, input().split()) #상자, 가로, 높이, 세로
    w, h, l = int(w), int(h), int(l)
    count = (w//12)*(h//12)*(l//12)
    if t == 'A':
        cnt += (w//12)*(h//12)*(l//12)
        amass += 500*(count)+1000
    else:
        bmass += 50*120

print(amass+bmass)
print(cnt*apple)