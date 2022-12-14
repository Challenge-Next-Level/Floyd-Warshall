import sys
from collections import defaultdict

T = int(input())

for _ in range(T):
    W = input().strip()
    K = int(input())
    alpha_dict = defaultdict(list)

    for t_idx in range(len(W)):
        t = W[t_idx]
        if W.count(t) >= K:
            alpha_dict[t].append(t_idx)

    if not alpha_dict:
        print(-1)
        continue

    min_str = sys.maxsize
    max_str = 0

    for idx_list in alpha_dict.values():
        for j in range(len(idx_list) - K + 1): # K 개 포함하고 있는 구간
            temp = idx_list[j + K - 1] - idx_list[j] + 1 # 해당 구간의 길이

            min_str = min(min_str, temp)
            max_str = max(max_str, temp)

    print(min_str, max_str)


