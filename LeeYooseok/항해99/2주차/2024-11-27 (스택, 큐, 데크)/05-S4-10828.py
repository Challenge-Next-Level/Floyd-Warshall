N = int(input())
stack = list()

for _ in range(N):
    user_input = input().split()
    command = user_input[0]

    if command == "push":
        X = int(user_input[1])
        stack.append(X)
    elif command == "pop":
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif command == "size":
        print(len(stack))
    elif command == "empty":
        if stack:
            print(0)
        else:
            print(1)
    elif command == "top":
        if stack:
            print(stack[-1])
        else:
            print(-1)
