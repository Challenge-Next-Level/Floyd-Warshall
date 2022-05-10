n = int(input())

tests = list(map(int, input().split()))

b, c = map(int, input().split())

result = 0

for t in tests:
    # 총 감독 1 명으로 커버 가능
    if t <= b:
        result += 1
    # 총 감독 1명으로 커버 불 가능
    else:
        # 총 감독관으로 커버 가능 부분 빼기
        result += 1
        temp = t - b

        # 필요한 부 감독관 확인
        if temp % c == 0:
            result += temp // c
        else:
            result += temp // c + 1

print(result)