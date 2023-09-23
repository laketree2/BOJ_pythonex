list = [1,2,3,4,5]

value = (list[2]-list[1])/(list[1]-list[0])

print(value)

isInt = int(value) == value
print(isInt)

if value != int(value):
    print('B')