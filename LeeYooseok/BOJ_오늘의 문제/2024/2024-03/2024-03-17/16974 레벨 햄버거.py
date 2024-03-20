N, X = map(int, input().split())

# 버거의 높이 - burger[i] = i 번째 버거의 높이
burger = [1] * 51
# 패티 개수 - patty[i] = i 번째 버거의 patty 개수
patty = [1] * 51

for i in range(1, N + 1):
    # 번 + i-1 버거 + 패티 + i - 1 버거 + 번
    burger[i] = 1 + burger[i - 1] + 1 + burger[i - 1] + 1

    # i-1 버거의 패티 개수 + 패티 + i-1 버거의 패티 개수
    patty[i] = patty[i - 1] + 1 + patty[i - 1]


def eat(n, x):
    # 버거의 레벨 0일 경우 -> 패티 한개
    if n == 0:
        return 1
    # 1층 -> 패티 0개
    if x == 1:
        return 0
    # 가운데 패티 이전 까지 먹은 경우 -> (n-1) 번 버거의 패티 개수
    elif x <= 1 + burger[n - 1]:
        return eat(n - 1, x - 1)  # 맨 아래 번 빼고 (x-1)
    # 가운데 패티 까지 먹은 경우
    elif x == 1 + burger[n - 1] + 1:
        return patty[n - 1] + 1
    # 가운데 패티 까지의 버거 높이 < 먹은 버거의 높이 < 전체 버거 높이
    elif x <= 1 + burger[n - 1] + 1 + burger[n - 1]:
        # n-1 버거의 (x - (1 + burger[n-1] + 1)) 의 높이 까지의 패티 개수
        return patty[n - 1] + 1 + eat(n - 1, (x - (1 + burger[n - 1] + 1)))
    # 전체 버거 다 먹은 경우
    else:
        return patty[n]

print(eat(N, X))
