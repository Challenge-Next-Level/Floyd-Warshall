N = int(input())
ans = 1
for i in range(1, N + 1):
    ans *= i
ans = str(ans)
for i in range(len(ans) - 1, -1, -1):

    if int(ans[i]) != 0:
        print(ans[i])
        break
