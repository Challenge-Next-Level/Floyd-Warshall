# 핵심 : S -> T 가 아닌 T -> S 로 하여 재귀 횟수를 줄인다.

S = input()
T = input()


def solve(t):
    if t == S:
        print(1)
        exit()

    if len(t) == 0:
        return

    if t[-1] == 'A':
        solve(t[:-1])

    if t[0] == 'B':
        solve("".join(reversed(t[1:])))

solve(T)
print(0)