a, b = 0, 1
answer = 0

n = int(input())

for i in range(1, n + 1):
    if i % 2 == 0:
        a += b
        a %= 1000000007
        answer = a
    else:
        b += a
        b %= 1000000007
        answer = b

print(answer)

