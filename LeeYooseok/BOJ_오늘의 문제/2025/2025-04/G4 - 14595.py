N = int(input())
M = int(input())

range_list = list()
for _ in range(M):
    x, y = map(int, input().split())
    range_list.append([x, y])

if M == 0:
    print(N)
    exit()

range_list.sort()

now_start, now_end = range_list[0]

answer = N
for new_start, new_end in range_list:
    if now_end >= new_start:
        now_end = max(now_end, new_end)
    else:
        answer -= (now_end - now_start)
        now_start, now_end = new_start, new_end

answer -= (now_end - now_start)

print(answer)
