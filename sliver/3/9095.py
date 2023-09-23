T = int(input())

for _ in range(T):
    n = int(input())
    count_list = [1, 2, 4]

    for i in range(4, n + 1):
        i = count_list[-1] + count_list[-2] + count_list[-3]
        count_list.append(i)

    if n == 1:
        answer = 1
    elif n == 2:
        answer = 2
    elif n == 3:
        answer = 4
    else:
        answer = count_list[-1]

    print(answer)