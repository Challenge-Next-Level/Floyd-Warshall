import sys
from itertools import combinations

N, M = map(int, input().split())
num_list = list(map(int, input().split()))

num_comb = combinations(num_list, 3)

answer = 0
diff = sys.maxsize

for comb in num_comb:
    if abs(M - sum(comb)) < diff and sum(comb) <= M:
        answer = sum(comb)
        diff = abs(M - answer)

print(answer)
