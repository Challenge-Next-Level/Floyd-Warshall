k, n = map(int, input().split())

wires = [int(input()) for _ in range(k)]
wires.sort()

# 시작을 0으로 했을때 zeroDivisionError 발생
left, right = 1, wires[-1]
mid = 0
answer = 0


def check(cm):
    total = 0
    for w in wires:
        total += w // cm

    if total >= n:
        return True
    else:
        return False


while left <= right:
    mid = (left + right) // 2
    if check(mid):
        left = mid + 1
        answer = max(mid, answer)
    else:
        right = mid - 1

print(answer)

