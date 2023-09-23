for i in range(int(input())):
    h, w, n = map(int, input().split()) #h층 w방 n번째손님방번호
    
    room = n//h+1
    floor = n % h

    if floor == 0:
        room = n//h
        floor = h
    print(floor*100+room)