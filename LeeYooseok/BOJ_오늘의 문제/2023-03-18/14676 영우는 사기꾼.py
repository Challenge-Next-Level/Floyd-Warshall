from collections import defaultdict

N, M, K = map(int, input().split())

graph = defaultdict(list)
for _ in range(M):
    a, b = map(int, input().split())
    graph[b].append(a)

constructed = [0] * (N + 1)

for _ in range(K):
    oper, param = map(int, input().split())

    if oper == 1:
        for prior_construct in graph[param]:
            if constructed[prior_construct] == 0:
                print("Lier!")
                exit()
        constructed[param] += 1
    else:
        if constructed[param] == 0:
            print("Lier!")
            exit()

        constructed[param] -= 1

print("King-God-Emperor")
