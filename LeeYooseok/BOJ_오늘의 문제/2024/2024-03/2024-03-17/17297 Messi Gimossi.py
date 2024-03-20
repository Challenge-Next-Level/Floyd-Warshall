M = int(input())

# messi 문자열의 길이
dp = [5, 13]
# 문자열의 길이가 M 보다 크거나 같을때까지 만들기
while dp[-1] < M:
    dp.append(dp[-2] + 1 + dp[-1])

def find(idx, M, dp):
    # idx 가 0 또는 1 이면 -> Messi Gimmosi 의 M 번째 문자열 반환
    if idx <= 1:
        return "Messi Gimossi"[M - 1]

    # M 이 messi[idx - 1] + 1 보다 크면 messi[idx - 2] 로 재귀
    if M > dp[idx - 1] + 1:
        res = find(idx - 2, M - dp[idx - 1] - 1, dp)
    # M 이 messi[idx - 1] 보다 작으면 messi[idx - 1] 로 재귀
    elif M < dp[idx - 1]:
        res = find(idx - 1, M, dp)
    # 딱 가운데 -> " " 반환
    else:
        return " "
    return res

answer = find(len(dp) - 1, M, dp)

if answer == " ":
    print("Messi Messi Gimossi")
else:
    print(answer)