X = list(input())

count = 0
while len(X) != 1:
    next_X = 0
    for i in range(len(X)):
        next_X += int(X[i])

    count += 1
    X = list(str(next_X))

print(count)
if int(X[0]) % 3 == 0:
    print("YES")
else:
    print("NO")