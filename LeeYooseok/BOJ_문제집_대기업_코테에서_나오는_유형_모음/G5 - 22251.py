n, k, p, x = map(int, input().split())

# 자릿수 맞춰주기 
if len(str(x)) < k:
    cx = '0' * (k - len(str(x))) + str(x)
else:
    cx = str(x)

num = ['1111110', '0110000', '1101101', '1111001', '0110011', '1011011',
       '1011111', '1110000', '1111111', '1111011']
arr = []

for i in range(10):
    arr.append([])
    for j in range(10):
        if i == j:
            arr[i].append(0)
        else:
            d = 0
            for h in range(7):
                if num[i][h] != num[j][h]:
                    d += 1
            arr[i].append(d)


def dfs(dep, cnt, cx):  # 깊이, 남은 반전 가능 횟수, 현재 문자열
    if dep >= len(cx):
        if int(cx) == x:  # 현재 층수와 결과가 같으면 안됨
            return 0
        elif 1 <= int(cx) <= n:  # 조건에 맞는 경우
            return 1
        else:  # 그외 경우는 불가능
            return 0

    rst, cur = 0, int(cx[dep])  # 정답, 현재 바꿔줄 숫자
    for i in range(10):
        if cur != i and (arr[cur][i] <= cnt):  # 남은 반전 가능 횟수보다 필요한 반전 횟수가 작아야 바꿀 수 있음
            dx = cx[:dep] + str(i) + cx[dep + 1:]
            rst += dfs(dep + 1, cnt - arr[cur][i], dx)

        elif cur == i:
            rst += dfs(dep + 1, cnt, cx)

    return rst


print(dfs(0, p, cx))