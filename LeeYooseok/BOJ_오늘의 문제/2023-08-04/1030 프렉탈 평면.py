s, N, K, R1, R2, C1, C2 = map(int, input().split())
size = N ** s  # 한 변의 길이


def check_black(_size, _y, _x):
    center = _size // N  # 검정색 칸 중심
    if _size == 1:
        return 0
    if center * (N - K) // 2 <= _x < center * (N + K) // 2 and center * (N - K) // 2 <= _y < center * (N + K) // 2:
        return 1
    _y %= center
    _x %= center
    return check_black(center, _y, _x)


for x in range(R1, R2 + 1):
    for y in range(C1, C2 + 1):
        print(check_black(size, y, x), end="")
    print()
