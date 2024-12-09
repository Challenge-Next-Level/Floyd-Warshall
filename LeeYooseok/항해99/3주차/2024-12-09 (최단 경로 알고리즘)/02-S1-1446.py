import sys

input = sys.stdin.readline

from collections import defaultdict

N, D = map(int, input().split())

distance_list = [i for i in range(D + 1)]

shortcut_dict = defaultdict(list)
for _ in range(N):
    s, e, c = map(int, input().split())
    shortcut_dict[e].append([s, c])

for i in range(1, D + 1):
    distance = distance_list[i - 1] + 1

    for start, cost in shortcut_dict[i]:
        if distance_list[start] + cost < distance:
            distance = distance_list[start] + cost

    distance_list[i] = distance

print(distance_list[-1])