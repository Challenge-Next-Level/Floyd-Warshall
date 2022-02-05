"""
- 문제 이해가 안됨
- 돌 1,3,4개일때, SK가 이긴다
    - 그 이후, i번째 에서 돌을 가져갔을 때 남아있는 돌의 갯수이 따른 승패여부 확인
"""


n = int(input())

dp = [0, True, False, True, True]

for i in range(5, n+1):
    if dp[i-1] and dp[i-3] and dp[i-4]: # 셋 다 모두 True(SK 승) 이면, 다음 차례인 CY 승
        dp.append(False)
    else:
        dp.append(True) # 셋 중 하나라도 False(CY 승)이면, 다음 차례인 SK 승

if dp[n]:
    print("SK")
else:
    print("CY")