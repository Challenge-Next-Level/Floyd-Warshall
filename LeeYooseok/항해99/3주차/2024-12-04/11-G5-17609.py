import sys

sys.setrecursionlimit(10**9)
input = sys.stdin.readline

T = int(input())


def solve(chance, left, right):
    global answer
    if not left <= right:
        if chance:
            answer = 0
        if not chance:
            answer = min(answer, 1)
        return
    if S[left] == S[right]:
        solve(chance, left + 1, right - 1)
    else:
        if chance:
            if S[left] == S[right - 1]:
                solve(False, left, right - 1)
            if S[left + 1] == S[right]:
                solve(False, left + 1, right)
            if S[left] != S[right - 1] and S[left + 1] != S[right]:
                return
        else:
            return


for _ in range(T):
    S = list(input().rstrip())

    c = True
    answer = 2
    l, r = 0, len(S) - 1

    solve(c, l, r)

    print(answer)
