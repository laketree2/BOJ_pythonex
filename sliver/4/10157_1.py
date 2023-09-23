import sys
input = sys.stdin.readline

C,R = map(int,input().split())

k = int(input())

#좌석을 줄 수 없는 경우 0처리
if k > C*R :
    print(0)
    exit()

#4방향 
dx = [0,1,0,-1]
dy = [-1,0,1,0]

#그리드 만들기 
arr = [[0]*C for _ in range(R)]
direction = x = y = 0


#행렬 돌면서 
for seat in range(1,C*R+1) :
    #내자리면 끝내기 
    if seat == k:
        print(y+1,x+1)
        break
    else :
        #표시하고 
        arr[x][y] = seat
        #앞으로 전진 
        x += dx[direction]
        y += dy[direction]
    
        if x<0 or y<0 or x>=R or y>=C or arr[x][y]:
            x -= dx[direction]
            y -= dy[direction]
            #범위 벗어나면 뒤로 뺐다가 방향 바꿔서 전진 
            direction = (direction+1)%4
            x += dx[direction]
            y += dy[direction]