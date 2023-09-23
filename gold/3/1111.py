n = int(input())
n_list = list(map(int, input().split()))
bp = 0

if n == 1:
    print('A')
    bp += 1
elif n == 2:
    if n_list[0] == n_list[1]:
        print(n_list[0])
        bp += 1
    else:
        print('A')
        bp += 1
# n >=3
elif n_list[1]-n_list[0] != 0:
    a = (n_list[2]-n_list[1]) / (n_list[1]-n_list[0])
    if (int(a) != a): 
        print("B")
        bp += 1
    elif (int(a) == a)and(n_list[0]==n_list[1]==n_list[2]) :
        a = int(a)
    b = n_list[1] - n_list[0]*a
else: #zerodivision
    a = 0
    b = n_list[1] 
    
if(bp == 0):
    for i in range(n-1):
        value = n_list[i] * a + b #앞수 * a + b [1,2,3,4,5]
        if(n_list[i+1] != value): 
            print('B')
            bp += 1
            break
    if(bp == 0):
        print(int(n_list[-1] * a + b))
    elif (len(set(n_list[1 : ])) == 1): 
        print(n_list[1])