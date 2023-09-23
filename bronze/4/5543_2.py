#햄버거 값 입력받기
ham_1 = int(input())
ham_2 = int(input())
ham_3 = int(input())
#음료수 값 입력받기
bev_1 = int(input())
bev_2 = int(input())

#최소값 구하기-햄버거
min_h = 3000 #햄버거 최소값 변수 선언, 모든 메뉴의 최대값은 2000원 이하

if ((ham_1<=ham_2)and(ham_1<=ham_3)):#최소값이 1번쨰 햄버거일 경우
    min_h = ham_1 
elif((ham_1>=ham_2)and(ham_2<=ham_3)):#최소값이 2번쨰 햄버거일 경우
    min_h = ham_2
elif((ham_1>=ham_3)and(ham_2>=ham_3)):#최소값이 3번쨰 햄버거일 경우
    min_h = ham_3
else: #햄버거 입력 값이 모두 같은 값일 경우
    min_h = ham_1 #값이 모두 같으므로 아무 햄버거나 최소값으로 지정, 1번째 지정

#최소값 구하기-음료수
min_b = 3000 #음료 최소값 변수 선언,모든 메뉴의 최대값은 2000원 이하
if (bev_1<=bev_2):#음료 리스트 값 중 1번째 값이 2번째 값보다 작을 경우
    min_b = bev_1 #1번째 값이 최소값이 됨
elif(bev_1>=bev_2): #2번째 값이 더 작을 경우
    min_b = bev_2 #2번째 값이 최소값이 됨
elif(bev_1==bev_2):#음료수 입력값이 모두 같을 때
    min_b = bev_1#최소값:첫번째 입력 값, 입력값이 모두 같기 때문
    

#결과값 출력
print(min_h+min_b-50) #햄버거 최소값+음료 최소값-50 =세트값