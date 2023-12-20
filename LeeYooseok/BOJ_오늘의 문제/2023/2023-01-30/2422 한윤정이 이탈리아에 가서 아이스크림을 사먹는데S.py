from collections import defaultdict

N, M = map(int, input().split())

no_mix_dict = defaultdict(list)
for _ in range(M):
    a, b = map(int, input().split())
    no_mix_dict[a].append(b)
    no_mix_dict[b].append(a)

answer = 0


def solve(visited, n, idx):
    global answer
    if n == 3:
        answer += 1
        return

    for i in range(idx, N + 1):
        if not visited[i]:
            new_visited = visited[:]
            new_visited[i] = True
            for flavor in no_mix_dict[i]:
                new_visited[flavor] = True

            solve(new_visited, n + 1, i + 1)


solve([False for _ in range(N + 1)], 0, 1)
print(answer)
