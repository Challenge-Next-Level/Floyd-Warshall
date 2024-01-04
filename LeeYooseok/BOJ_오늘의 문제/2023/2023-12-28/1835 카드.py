from collections import deque

N = int(input())

answer = deque(list())

for n in range(N, 0, -1):
    answer.appendleft(n)

    if (len(answer) > 1):
        for _ in range(n):
            answer.appendleft(answer.pop())

print(*answer)