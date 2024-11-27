while True:
    S = input()

    if S == ".":
        break

    stack = list()

    for s in S:
        if s == "(" or s == "[":
            stack.append(s)
        elif s == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(")")
        elif s == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                stack.append("]")

    if stack:
        print("no")
    else:
        print("yes")