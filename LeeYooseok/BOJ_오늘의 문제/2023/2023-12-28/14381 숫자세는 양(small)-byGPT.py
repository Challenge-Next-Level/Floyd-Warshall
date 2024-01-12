# INSOMNIA 는 0 빼고 200까지는 없음
T = int(input())


def check(N):
    seen = set()
    i = 1
    while len(seen) < 10:
        current = i * N
        seen.update(str(current))
        i += 1
    return current


for t in range(1, T + 1):
    N = int(input())

    print("Case #{}: {}".format(t, check(N)))