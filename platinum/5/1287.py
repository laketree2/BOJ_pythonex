import re

def calculate_expression(expression):
    try:
        # 수식에 있는 모든 공백 제거
        expression = expression.replace(" ", "")

        # 수식에서 숫자와 연산자 분리하여 리스트로 저장
        tokens = re.findall(r'\d+|\+|\-|\*|\/|\^|\(|\)', expression)

        # 연산자의 우선순위를 정의한 딕셔너리
        precedence = {'^': 3, '*': 2, '/': 2, '+': 1, '-': 1}

        # 중위 표기식을 후위 표기식으로 변환
        postfix = []
        operator_stack = []

        for token in tokens:
            if token.isdigit():
                postfix.append(token)
            elif token == '(':
                operator_stack.append(token)
            elif token == ')':
                while operator_stack and operator_stack[-1] != '(':
                    postfix.append(operator_stack.pop())
                operator_stack.pop()  # '(' 제거
            else:
                while (operator_stack and operator_stack[-1] != '(' and
                       precedence.get(token, 0) <= precedence.get(operator_stack[-1], 0)):
                    postfix.append(operator_stack.pop())
                operator_stack.append(token)

        while operator_stack:
            postfix.append(operator_stack.pop())

        # 후위 표기식 계산
        operand_stack = []

        for token in postfix:
            if token.isdigit():
                operand_stack.append(int(token))
            else:
                b = operand_stack.pop()
                a = operand_stack.pop()

                if token == '+':
                    operand_stack.append(a + b)
                elif token == '-':
                    operand_stack.append(a - b)
                elif token == '*':
                    operand_stack.append(a * b)
                elif token == '/':
                    operand_stack.append(a // b)
                elif token == '^':
                    operand_stack.append(a ** b)

        return operand_stack[0]

    except:
        return "ERROR"

# 입력 받아서 결과 출력
expression = input()
result = calculate_expression(expression)
print(result)
