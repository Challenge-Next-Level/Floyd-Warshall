N = int(input())


# sqrt 구현
def custom_sqrt(n):
    start = 0
    end = n

    while start <= end:
        mid = (start + end) // 2

        if mid ** 2 == n:
            return mid

        elif mid ** 2 < n:
            start = mid + 1
        else:
            end = mid - 1

    return -1


print(custom_sqrt(N))
