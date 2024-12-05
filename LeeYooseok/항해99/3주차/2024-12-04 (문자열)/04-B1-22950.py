N = int(input())
M = list(map(int, input()))
K = int(input())

if 1 not in M:
    print('YES')
    exit(0)
if K == 0:
    print('YES')
    exit(0)

zero_count = 0
for i in range(N - 1, -1, -1):
    if M[i] == 0:
        zero_count += 1
        if K == zero_count:
            break
    else:
        break


if K == zero_count:
    print("YES")
else:
    print("NO")