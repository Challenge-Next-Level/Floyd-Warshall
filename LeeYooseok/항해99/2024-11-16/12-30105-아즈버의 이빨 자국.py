from collections import defaultdict

N = int(input())
x_list = list(map(int, input().split()))

answer = set()

diff_dict = defaultdict(set)

for i in range(N):
    for j in range(i + 1, N):
        diff = x_list[j] - x_list[i]

        diff_dict[diff].add(x_list[i])
        diff_dict[diff].add(x_list[j])

        if len(diff_dict[diff]) == N:
            answer.add(diff)

print(len(answer))
print(*sorted(answer))