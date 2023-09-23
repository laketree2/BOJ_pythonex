n = int(input())
info = []
lens = []
for i in range(n):
    x, y = map(int, input().split())
    route = list()
    #'W', 'E', 'D', 'C', 'X', 'Z', 'A', 'Q'(시계방향)
    while (x, y) != (0, 0):
        if x > 0:
            x -= 1
            if y > 0:
                y -= 1
                route.append('Z')
            elif y < 0:
                y += 1
                route.append('Q')
            else:
                route.append('A')
        elif x < 0:
            if y > 0:
                y -= 1
                route.append('C')
            elif y < 0:
                y += 1
                route.append('D')
            else:
                route.append('E')
        else:
            if y > 0:
                y -= 1
                route.append('X')
            else:
                y += 1
                route.append('W')
    # 이동 개수 리스트에 담고 앞 순서보다 짧거나 같으면 안되게
    # if len(route[0]) < len(route[1]):
    print(route)
    info.append(route)
for k in info:
    print(*k, sep = '')