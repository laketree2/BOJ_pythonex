number = []
for i in range(5):
    #n = int(input())
    #num.append(n)
    number.append(int(input()))
    
number.sort()

print(int(sum(number)/5))
print(number[2])