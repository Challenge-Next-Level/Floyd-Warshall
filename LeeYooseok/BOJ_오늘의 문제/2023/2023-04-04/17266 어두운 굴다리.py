N = int(input())
M = int(input())
X = list(map(int, input().split()))


def check(height):
    if X[0] > height:
        return False

    for idx in range(M - 1):
        if (X[idx + 1] - X[idx]) > 2 * height:
            return False

    if (N - X[M - 1]) > height:
        return False

    return True


start, end = 0, N
answer = 1e9

while start <= end:
    mid = (start + end) // 2

    if check(mid):
        answer = min(answer, mid)
        end = mid - 1
    else:
        start = mid + 1

print(answer)
