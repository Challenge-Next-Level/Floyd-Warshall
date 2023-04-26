N, K = map(int, input().split())
num_set = list(map(int, input().split()))
num_set.sort(reverse=True)

ans = 0


def solve(now_ans):
    global ans
    for num in num_set:
        new_ans = 10 * now_ans + num

        if new_ans <= N:
            solve(new_ans)
            ans = max(ans, new_ans)


solve(0)

print(ans)
