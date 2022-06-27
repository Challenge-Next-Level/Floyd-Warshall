str1 = input()

result = ''
# 연산자만 다 넣어둠
stack = list()

for s in str1:
    # 알파벳이면 바로 결과에 추가
    if s.isalpha():
        result += s
    else:
        # s 가 열린괄호 이면
        if s == '(':
            stack.append(s)
        # s 가 * 또는 / 이면, 우선순위 확인
        elif s == '*' or s == '/':
            # 먼저 들어오고 같은 우선순위에 있는 *, /는 result 에 넣어줌
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                result += stack.pop()
            stack.append(s)
        elif s == '+' or s == '-': # 이보다 낮은 우선 순위가 없어서 연산자이면 전부 result 에 넣어줌
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.append(s)
        elif s == ')': # 닫음 괄호와 열음 괄호 사이에 있는 연산자들 전부 반환
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.pop()

print(result)