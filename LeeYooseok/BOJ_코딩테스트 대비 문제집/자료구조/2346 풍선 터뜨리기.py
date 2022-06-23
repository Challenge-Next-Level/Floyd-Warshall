from collections import deque
N = int(input())

input_list = list(map(int, input().split()))

queue = list()

for i in range(len(input_list)):
    queue.append([input_list[i], i+1])

queue = deque(queue)

while queue:
    move = queue.popleft()
    print(move[1], end=" ")

    if queue:
        if move[0] > 0:
            for _ in range(move[0] - 1):
                queue.append(queue.popleft())
        elif move[0] < 0:
            for _ in range(-1 * move[0]):
                queue.insert(0, queue.pop())