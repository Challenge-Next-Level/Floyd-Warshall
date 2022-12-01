N = int(input())

num_list = [0]

for _ in range(N):
    num_list.append(int(input()))

answer = set()


def dfs(first, second, num):
    first.add(num)
    second.add(num_list[num])
    if num_list[num] in first:
        if first == second:
            answer.update(first)
            return True
        return False
    dfs(first, second, num_list[num])


for idx in range(1, N + 1):
    if idx not in answer:
        dfs(set(), set(), idx)

print(len(answer))
for n in sorted(list(answer)):
    print(n)