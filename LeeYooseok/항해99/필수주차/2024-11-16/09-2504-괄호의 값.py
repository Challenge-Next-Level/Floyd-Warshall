S = input()

stack = []
answer = 0
temp = 1
for i in range(len(S)):
    if S[i] == "(":
        temp *= 2
        stack.append(S[i])

    elif S[i] == "[":
        temp *= 3
        stack.append(S[i])

    elif S[i] == ")":
        # stack 이 비어있거나 마지막이 "(" 가 아니면, 잘못된 괄호
        if not stack or stack[-1] != "(":
            answer = 0
            break

        # 괄호가 닫힌다면, answer에 임시 값 더해주고 현재 값을 2를 나눠준다.
        if S[i - 1] == "(":
            answer += temp
        temp = temp // 2
        stack.pop()

    elif S[i] == "]":
        # stack 이 비어있거나 마지막이 "[" 가 아니면, 잘못된 괄호
        if not stack or stack[-1] != "[":
            answer = 0
            break

        # 괄호가 닫힌다면, answer에 임시 값 더해주고 현재 값을 3을 나눠준다.
        if S[i - 1] == "[":
            answer += temp
        temp = temp // 3
        stack.pop()

if stack:
    print(0)
else:
    print(answer)
