import sys

input = sys.stdin.readline

N, X = map(int, input().split())

visit_list = list(map(int, input().split()))

prefix_sum = [sum(visit_list[:X])]
for idx in range(N - X):
    prefix_sum.append(prefix_sum[-1] + visit_list[X + idx] - visit_list[idx])

max_visit = max(prefix_sum)

if max_visit == 0:
    print("SAD")
else:
    print(max_visit)
    print(prefix_sum.count(max_visit))