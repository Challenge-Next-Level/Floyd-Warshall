n, m = map(int, input().split())
w1 = input()
w2 = input()

# 입력문자와 결과문자의 편집거리를 저장할 이차원 배열 dp를 생성하여 초기화한다.
dp = [[i] + [0] * m for i in range(n + 1)]

# 입력문자, 결과문자 각각을 모두 지우기 위한 값 추가
dp[0] = [i for i in range(m + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
        # 비교문자가 같은 경우 -> 대각선 방향의 숫자를 그대로 가져와 저장한다.
        if w1[i - 1] == w2[j - 1] or (w1[i - 1] == 'v' and w2[j - 1] == 'w') or (w1[i - 1] == 'i' and w2[j - 1] in ['j', 'l']):
            dp[i][j] = dp[i - 1][j - 1]
print(dp[n][m])