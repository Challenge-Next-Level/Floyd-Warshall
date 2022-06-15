N = int(input())
numbers = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, N):
    for idx in range(len(numbers[i])):
        if idx == 0:
            numbers[i][idx] = numbers[i][idx] + numbers[i-1][idx]
        elif idx == i:
            numbers[i][idx] = numbers[i][idx] + numbers[i-1][idx - 1]
        else:
            numbers[i][idx] = max(numbers[i-1][idx-1] + numbers[i][idx], numbers[i-1][idx] + numbers[i][idx])

print(max(numbers[N-1]))