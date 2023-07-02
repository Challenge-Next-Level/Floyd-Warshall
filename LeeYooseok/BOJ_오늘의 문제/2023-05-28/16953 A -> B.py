A, B = map(int, input().split())

answer = 0
while A < B:
    if B % 2 == 0:
        B /= 2
    elif (B % 10) == 1:
        B = B // 10
    else:
        break
    answer += 1

if B == A:
    print(answer + 1)
else:
    print(-1)