import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    l, n = map(int, input().split())
    ant_location = list()
    for _ in range(n):
        ant_location.append(int(input()))

    ant_location.sort()
    min_time = 0
    max_time = 0

    for ant in ant_location:
        min_time = max(min_time, min(ant, l - ant))
        max_time = max(max_time, ant, l-ant)
    print(min_time, max_time)
