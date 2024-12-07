N = int(input())

answer = 10

n = 1
while N >= n * 2:
    answer += 1
    n *= 2

print(answer)
