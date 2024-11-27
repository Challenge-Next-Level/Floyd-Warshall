answer = ["-" for _ in range(3 ** 12)]


def solve(n, start):
    global answer

    if n == 0:
        return

    for i in range(start + (3 ** (n - 1)), start + 2 * (3 ** (n - 1))):
        answer[i] = " "
    solve(n - 1, start)
    solve(n - 1, start + 2 * (3 ** (n - 1)))


solve(12, 0)

while True:
    try:
        N = int(input())
        print("".join(answer[:3**N]))
    except:
        break
