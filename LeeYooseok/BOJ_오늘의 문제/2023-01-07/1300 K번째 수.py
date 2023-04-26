# https://kbw1101.tistory.com/29

# K 번째 숫자를 S 라 했을 때, S 보다 작거나 같은 숫자들의 개수가 K 보다 작으면 안된다.
# 만약 작다면, S 가 더 커져야 한다.
# 만약 많다면, S 가 더 작아져야 한다.

N = int(input())
K = int(input())

left, right = 1, K
answer = 0
while left <= right:
    S = (left + right) // 2

    cnt = 0
    for i in range(1, N + 1):
        # A 보드에 i 번째 행에 S 보다 작거나 같은 수들의 개수
        cnt += min(S // i, N)

    if cnt >= K:
        right = S - 1
        answer = S
    else:
        left = S + 1

print(answer)