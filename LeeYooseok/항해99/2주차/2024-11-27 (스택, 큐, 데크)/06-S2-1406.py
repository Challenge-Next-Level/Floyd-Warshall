import sys

input = sys.stdin.readline

from collections import deque

# 초기에 커서는 문장의 맨 뒤에 위치하고 있음
left_text = deque(list(input().rstrip()))
right_text = deque(list())

M = int(input())
for _ in range(M):
    user_input = list(input().split())

    command = user_input[0]

    # 커서를 왼쪽으로 한칸 옮김
    if command == "L":
        if left_text:
            right_text.appendleft(left_text.pop())
    # 커서를 오른쪽으로 한칸 옮김
    elif command == "D":
        if right_text:
            left_text.append(right_text.popleft())
    # 커서 왼쪽에 있는 문자를 삭제함
    elif command == "B":
        if left_text:
            left_text.pop()
    # $ 라는 문자를 커서 왼쪽에 추가함
    elif command == "P":
        x = user_input[1]
        left_text.append(x)

print("".join(left_text) + "".join(right_text))