import sys

input = sys.stdin.readline

from collections import deque

N = int(input())

que = deque(list())

for _ in range(N):
    user_input = list(input().split())

    command = user_input[0]
    if len(user_input) == 2:
        param = int(user_input[1])

    if command == "push":
        que.append(param)
    elif command == "pop":
        if que:
            print(que.popleft())
        else:
            print(-1)
    elif command == "size":
        print(len(que))
    elif command == "empty":
        if que:
            print(0)
        else:
            print(1)
    elif command == "front":
        if que:
            print(que[0])
        else:
            print(-1)
    elif command == "back":
        if que:
            print(que[-1])
        else:
            print(-1)