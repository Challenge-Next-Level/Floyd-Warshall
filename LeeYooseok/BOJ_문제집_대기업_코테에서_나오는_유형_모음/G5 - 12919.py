S = list(input())
T = list(input())

answer = 0


def solve(t):
    global answer
    if t == S:
        print(1)
        exit()

    if not t:
        return

    if t[-1] == "A":
        solve(t[:-1])

    if t[0] == "B":
        solve(t[1:][::-1])


solve(T)

print(answer)