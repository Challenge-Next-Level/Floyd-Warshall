from collections import deque

N = int(input())
deq = deque([(i + 1) for i in range(N)])

turn = 0
while len(deq) > 1:
    if turn == 0:
        deq.popleft()
        turn = 1
    else:
        deq.append(deq.popleft())
        turn = 0

print(deq[0])