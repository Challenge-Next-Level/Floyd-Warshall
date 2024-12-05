N = int(input())
paper_list = list(map(int,input().split()))

balloon_list = list()
for i in range(N):
    balloon_list.append([i + 1, paper_list[i]])


now_idx = 0
answer = list()
while len(balloon_list) > 1:
    idx, value = balloon_list.pop(now_idx)
    answer.append(idx)

    if value > 0:
        now_idx = ((now_idx - 1 + value) % len(balloon_list))
    else:
        now_idx = ((now_idx + value) % len(balloon_list))

answer.append(balloon_list.pop()[0])

print(*answer)