import sys
from collections import defaultdict

input = sys.stdin.readline

N, X = map(int, input().split())
visit_count_list = list(map(int, input().split()))

visit_count_dict = defaultdict(int)

sum_visit = sum(visit_count_list[:X])
max_visit = sum_visit
visit_count_dict[sum_visit] += 1

for i in range(N - X):
    sum_visit = sum_visit - visit_count_list[i] + visit_count_list[X + i]
    max_visit = max(max_visit, sum_visit)
    visit_count_dict[sum_visit] += 1

if max_visit == 0:
    print("SAD")
else:
    print(max_visit)
    print(visit_count_dict[max_visit])