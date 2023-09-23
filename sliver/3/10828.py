#클래스 정의
class Stack:
    def __init__(self): #인스턴스를 만들 때 호출, 객체 초기화
        self.len = 0 #길이 초기화
        self.list = [] #리스트 초기화
        
    def push(self,num): #정수를 스택에 넣기 위한 함수 선언
        self.list.append(num) #리스트에 값 추가
        self.len +=1 #길이 늘리기
        
    def pop(self): #스택에서 가장 위에 있는 정수를 빼고 그 수를 출력하기 위한 함수 선언
        if self.size()==0:#아무것도 들어있지 않을 때
            return -1 #출력
        pop_result = self.list[self.len - 1] #스택의 가장 위의 있는 정수 리턴 
        del self.list[self.len - 1] #그 값 지우기
        self.len -= 1 #길이 줄이기
        return pop_result #값 리턴
    
    def size(self): #스택에 들어있는 정수의 개수를 출력하기 위한 메서드 선언
        return self.len #정수 개수 == 길이 리턴
    
    def empty(self): #스택이 비어있을 때 출력할 함수 선언
        if self.len == 0: #비어있지 않으면
            return 1 #값 리턴
        else: #비어있으면
            return 0 #리턴
        
    def top(self): #스택의 가장 위에 있는 정수를 출력하기 위한 메서드
        if self.size() !=0: #스택이 비어있다면
            return self.list[-1] #리턴
        else: #비어있다면
            return -1 #리턴
        
num = int(input()) #값 입력받기
stack = Stack() #함수 호출
for _ in range(num): #반복
    cmd = input().split() #명령 입력받기
    
    op = cmd[0] #변수 할당
    
    if op =="push": #입력 요청값이 push면
        stack.push(cmd[1]) #할당
    elif op == "pop": #입력 요청값이 pop이면
        print(stack.pop()) #출력
    elif op =="size":#입력 요청값이 push면
        print(stack.size()) #출력
    elif op == "empty":#입력 요청값이 push면
        print(stack.empty) #출력
    elif op =="top":#입력 요청값이 push면
        print(stack.top()) #출력
    else: #모두 해당되지 않으면
        print("unacceptable op") #출력