n = int(input())

start, end = 0, n

answer = n

while start <= end:
    mid = (start + end) // 2

    if mid ** 2 >= n:
        answer = mid
        end = mid - 1
    else:
        start = mid + 1

print(answer)