N, K = map(int, input().split())
HP_list = ["-"] * K + list(input()) + ["-"] * K

answer = 0
visited = [False for _ in range(N + 2 * K)]
# 우선순위 -> (앞 -> 뒤)
for i in range(N):
    if HP_list[K + i] == "P":
        for k in range(i, 2 * K + i + 1):
            if HP_list[k] == "H" and not visited[k]:
                visited[k] = True
                answer += 1
                break

print(answer)