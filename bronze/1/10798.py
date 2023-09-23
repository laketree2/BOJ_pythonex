'''
문자 입력받아서 세로로 출력
★2차원 배열로 보기
단어 입력받을 때 길이 함께 저장
길이가 제일 긴 만큼 반복
단어의 수 = 5 반복
해당 단어에 맞는 글자마다 문자열 추가
세로로 읽은 순서대로 출력(문자열 저장)
'''

'''
null 배열 생성 
열 리스트 안에 요소
행 가로줄

'''
'''
ABCDE
abcde
01234
FGHIJ
fghij
 
AABCDD
afzz
09121
a8EWg6
P5h3kx
'''

def read_vertical(strings):
    read_string = []
    max_len = max([len(string) for string in strings])
    
    for i in range(max_len):
        for string in strings:
            if len(string) - 1 >= i:
                read_string.append(string[i])
    return "".join(read_string)
    
if __name__ == "__main__":
    strings = []
    for _ in range(5):
        string = input()
        strings.append(string)
    print(read_vertical(strings))