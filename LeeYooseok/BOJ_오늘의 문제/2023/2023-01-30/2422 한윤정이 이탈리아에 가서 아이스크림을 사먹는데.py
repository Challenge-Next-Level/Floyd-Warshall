from collections import defaultdict
from itertools import combinations
N, M = map(int, input().split())

no_mix_dict = defaultdict(list)
for _ in range(M):
    a, b = map(int, input().split())
    no_mix_dict[a - 1].append(b - 1)
    no_mix_dict[b - 1].append(a - 1)

answer = 0

for i in combinations(range(N), 3):
    if i[0] in no_mix_dict[i[1]] or i[1] in no_mix_dict[i[2]] or i[2] in no_mix_dict[i[0]]:
        continue
    answer += 1
print(answer)
