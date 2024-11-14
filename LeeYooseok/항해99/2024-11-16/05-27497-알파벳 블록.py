import sys

input = sys.stdin.readline

from collections import deque

N = int(input())

deq = deque(list())
append_list = list()

for _ in range(N):
    operator_list = input().rstrip().split()

    if operator_list[0] == "1":
        deq.append(operator_list[1])
        append_list.append(1)
    elif operator_list[0] == "2":
        deq.appendleft(operator_list[1])
        append_list.append(2)
    else:
        if deq:
            if append_list.pop() == 1:
                deq.pop()
            else:
                deq.popleft()

if len(deq) == 0:
    print(0)
else:
    print("".join(deq))