import sys

N, M = map(int, sys.stdin.readline().split())
spot = list(map(int, sys.stdin.readline().split()))
spot.sort()


def binary_search(s, e):
    left, right = 0, N - 1
    mid = 0
    while left <= right:
        mid = (left + right) // 2
        if e >= spot[mid] >= s:
            right = mid - 1
        else:
            if spot[mid] < s:
                left = mid + 1
            else:
                right = mid - 1
    return mid


def binary_search_reverse(s, e):
    left, right = 0, N - 1
    mid = 0
    while left <= right:
        mid = (left + right) // 2
        if s <= spot[mid] <= e:
            left = mid + 1
        else:
            if spot[mid] > e:
                right = mid - 1
            else:
                left = mid + 1
    return mid


for _ in range(M):
    start, end = map(int, sys.stdin.readline().split())

    left_idx = binary_search(start, end)
    right_idx = binary_search_reverse(start, end)
    if start <= spot[left_idx] and spot[right_idx] <= end:
        answer = right_idx - left_idx + 1
    elif start > spot[left_idx] and spot[right_idx] > end:
        answer = right_idx - left_idx - 1
    else:
        answer = right_idx - left_idx

    print(answer)
