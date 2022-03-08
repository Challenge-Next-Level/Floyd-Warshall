n, m = map(int, input().split())

trees = list(map(int, input().split()))
trees.sort()

left, right = 0, max(trees)
mid = trees[-1]
answer = 0


def check(h):
    total = 0
    for t in trees:
        if t > h:
            total += t - h

    if total >= m:
        return True
    else:
        return False


while left <= right:
    mid = (left + right) // 2

    if check(mid):
        left = mid + 1
        answer = max(answer, mid)
    else:
        right = mid - 1

print(answer)
