import sys

input = sys.stdin.readline

n = int(input())
snows = list(map(int, input().split()))

snows.sort()

result = sys.maxsize

for i in range(n-1):
    for j in range(i, n):# 눈사람 1을 만들 수 있는 모든 경우의 수
        first_snowman = snows[i] + snows[j]

        start = 0
        end = n-1

        while start < end:
            # 이미 첫번째 눈사람에서 쓰인 눈이라면,
            if start == i or start == j:
                start += 1
                continue

            if end == i or end == j:
                end -= 1
                continue

            second_snowman = snows[start] + snows[end]

            diff = first_snowman - second_snowman

            result = min(result, abs(diff))

            # pointer 이동
            if diff < 0:
                # 두번째 눈사람이 더 크므로 크기를 줄여야 함
                end -= 1
            else:
                start += 1


print(result)

