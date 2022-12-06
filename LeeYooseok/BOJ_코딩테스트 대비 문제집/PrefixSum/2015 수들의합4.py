from collections import defaultdict

import sys

input = sys.stdin.readline

N, K = map(int, input().split())
num_list = list(map(int, input().split()))

prefix_sum = 0
prefix_sum_dict = defaultdict(int) # 부분합이 K (key) 인 구간의 개수 (value)
prefix_sum_dict[0] = 1 # 부분합이 K 일때 즉, 구간이 처음부터 특정 숫자까지 일때 -> 구간 [0, i]
answer = 0

for n in num_list:
    prefix_sum += n

    if (prefix_sum - K) in prefix_sum_dict.keys(): # prefix_sum_dict 의 key 들 중 prefix_sum 과의 차가 K 이면 : 해당 구간의 부분합이 K 이면,
        answer += prefix_sum_dict[prefix_sum - K]

    prefix_sum_dict[prefix_sum] += 1

print(answer)
