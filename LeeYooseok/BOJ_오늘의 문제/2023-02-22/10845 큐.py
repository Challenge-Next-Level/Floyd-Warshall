import sys

input = sys.stdin.readline

N = int(input())

que = list()

for _ in range(N):
    commands = list(input().split())

    operation = commands[0]
    if len(commands) == 2:
        param = int(commands[1])

    if operation == "push":
        que.append(param)
    elif operation == "pop":
        if que:
            print(que.pop(0))
        else:
            print(-1)
    elif operation == "size":
        print(len(que))
    elif operation == "empty":
        if que:
            print(0)
        else:
            print(1)
    elif operation == "front":
        if que:
            print(que[0])
        else:
            print(-1)
    elif operation == "back":
        if que:
            print(que[-1])
        else:
            print(-1)