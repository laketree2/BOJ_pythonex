croatia = ['c=','c-','dz=','d-','lj','nj','s=','z='] #크로아티아 문자에 해당되는 글자 리스트로 묶음

a = input() #문자 입력받기
count = 0 #크로아티아 문자 개수 받을 변수 초기화
for i in range(len(a)):
    if ('c='or'c-'or'dz='or'd-'or'lj'or'nj'or's='or'z=') in :
        count +=1 # 개수 추가
print(count) #추가된s 개수만큼의 길이 출력 