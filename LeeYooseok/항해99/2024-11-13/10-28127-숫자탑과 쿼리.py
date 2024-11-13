import sys

input = sys.stdin.readline

Q = int(input())
for _ in range(Q):
    a, d, x = map(int, input().split())

    i, total = 1, 0
    while True:
        now_block = a + (i - 1) * d
        # 현재 층에서 블럭 개수 만족 시, break -> total = 이전 층 까지의 블럭 개수
        if total + now_block >= x:
            break
        # 블럭 개수 증가
        total += now_block
        # 층수 증가
        i += 1

    print(i, x - total)