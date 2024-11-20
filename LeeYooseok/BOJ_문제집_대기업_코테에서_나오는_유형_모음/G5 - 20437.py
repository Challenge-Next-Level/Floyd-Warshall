import sys

input = sys.stdin.readline

from collections import defaultdict

T = int(input())

for _ in range(T):
    W = input().rstrip()
    K = int(input())

    alpha_dict = defaultdict(list)

    # K개 이상인 alphabet 확인
    for idx in range(len(W)):
        alphabet = W[idx]

        if W.count(alphabet) >= K:
            alpha_dict[alphabet].append(idx)


    # K개 이상인 alphabet이 없다면
    if not alpha_dict:
        print(-1)
        continue

    # 정답 변수
    min_str = sys.maxsize
    max_str = 0

    for idx_list in alpha_dict.values():
        for j in range(len(idx_list) - K + 1):  # K개를 포함하고 있는 구간
            # 해당 구간의 길이
            temp = idx_list[j + K - 1] - idx_list[j] + 1

            min_str = min(min_str, temp)
            max_str = max(max_str, temp)

    print(min_str, max_str)