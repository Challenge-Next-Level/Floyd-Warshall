N = int(input())

work_list = list()
for _ in range(N):
    t, s = map(int, input().split())
    work_list.append([s, t])

work_list.sort()

total_time = 0
answer = 1e9
for s, t in work_list:
    total_time += t
    answer = min(answer, s - total_time)
    if s < total_time:
        print(-1)
        exit()
print(answer)