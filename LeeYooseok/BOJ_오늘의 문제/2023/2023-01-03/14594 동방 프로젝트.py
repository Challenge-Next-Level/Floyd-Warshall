N = int(input())
rooms = [1] * (N + 1)

M = int(input())
for _ in range(M):
    x, y = map(int, input().split())

    for idx in range(x, y):
        if rooms[idx] == 1:
            rooms[idx] = 0

print(sum(rooms) - 1)