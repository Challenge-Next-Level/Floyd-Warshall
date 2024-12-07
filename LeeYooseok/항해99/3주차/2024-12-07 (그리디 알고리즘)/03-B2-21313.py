N = int(input())

answer = [1, 2] * (N // 2)
if N % 2 != 0:
    answer.append(3)

print(*answer)