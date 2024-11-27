N, K = map(int, input().split())

answer = list()

people_list = [(i + 1) for i in range(N)]
now_idx = K - 1
while people_list:
    answer.append(people_list.pop(now_idx))
    if people_list:
        now_idx = ((now_idx - 1 + K) % len(people_list))

print('<' + ", ".join(list(map(str, answer))) + '>')
