import sys

input = sys.stdin.readline

X, Y = map(int, input().split())

# 승률
Z = (100 * Y) // X
# 이분 탐색 : 승률을 높이기 위해, 이겨야 할 게임 수
left, right = 0, X
answer = X

if Z >= 99:
    print(-1)
else:
    while left <= right:
        mid = (left + right) // 2
        # mid 번 더 이겨서, 승률이 오른다면,
        if (100 * (Y + mid)) // (X + mid) > Z:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    print(answer)