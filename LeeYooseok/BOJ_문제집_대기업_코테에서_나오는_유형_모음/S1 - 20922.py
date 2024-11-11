import sys

input = sys.stdin.readline

from collections import defaultdict

N, K = map(int, input().split())
number_list = list(map(int, input().split()))

left, right = 0, 0
number_dict = defaultdict(int)
answer = 0

while right < N:
    now_num = number_list[right]

    if number_dict[now_num] < K:
        number_dict[now_num] += 1
        right += 1
        answer = max(answer, right - left)
    else:
        number_dict[number_list[left]] -= 1
        left += 1

print(answer)