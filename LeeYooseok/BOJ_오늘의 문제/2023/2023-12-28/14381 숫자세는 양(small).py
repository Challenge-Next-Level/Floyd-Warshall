# INSOMNIA 는 0 빼고 200까지는 없음
import sys
sys.setrecursionlimit(10**6)
T = int(input())


def check(n, x):
    global num_check
    for _n in str(n * x):
        if not num_check[int(_n)]:
            num_check[int(_n)] = True

    if False not in num_check:
        return n * x
    else:
        return check(n, x + 1)


for t in range(1, T + 1):
    N = int(input())

    num_check = [False for _ in range(10)]
    print("Case #{}: {}".format(t, check(N, 1)))
