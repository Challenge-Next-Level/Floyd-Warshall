N = int(input())

idx_list = [0]
now_degree = 0
while True:
    if 2 ** (now_degree + 1) > N:
        break
    idx_list.append(now_degree + 1)
    now_degree += 1

prior_value_list = [0, 1, 3, 4]
answer = 0
while N > 3:
    now_idx = idx_list[-1]
    idx_list.pop()
    if N < 2 ** now_idx:
        continue
    N -= 2 ** now_idx
    answer += 3 ** now_idx

answer += prior_value_list[N]

print(answer)