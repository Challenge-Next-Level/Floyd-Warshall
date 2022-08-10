import sys

n, k = map(int, input().split())
s = set() # 동전의 종류를 set으로 정리
for _ in range(n):
    s.add(int(sys.stdin.readline()))

s = list(s)
s.sort()

dp = [-1 for _ in range(100001)] # dp 세팅
size = len(s) # 동전의 갯수는 중복 가능성이 있어 다시 설정한다.
for i in range(size):
    dp[s[i]] = 1

for i in range(1,k+1):
    for j in range(size):
        num = i - s[j]
        if num <= 0:
            break
        if dp[num] == -1:
            continue
        if dp[i] != -1:
            dp[i] = min(dp[i], dp[num] + 1)
        else:
            dp[i] = dp[num] + 1
print(dp[k])