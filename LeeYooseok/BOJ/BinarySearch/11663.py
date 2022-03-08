n, m = map(int, input().split())

points = list(map(int, input().split()))
points.sort()


# 시작 지점 검색 : 시작 지점보다 크거나 같은 수의 위치 반환
def search(s, e):
    left, right = 0, n - 1
    mid = 0
    while left <= right:
        mid = (left + right) // 2
        if s <= points[mid] <= e:
            right = mid - 1
        else:
            if points[mid] < s:
                left = mid + 1
            else:
                right = mid - 1
    return mid


# 끝 지점 검색 : 종료 지점보다 작거나 같은 수의 위치 반환
def reverse_search(s, e):
    left, right = 0, n - 1
    mid = 0
    while left <= right:
        mid = (left + right) // 2
        if s <= points[mid] <= e:
            left = mid + 1
        else:
            if points[mid] > e:
                right = mid - 1
            else:
                left = mid + 1
    return mid


for _ in range(m):
    start, end = map(int, input().split())

    left_idx = search(start, end)
    right_idx = reverse_search(start, end)

    # start 가 left_idx 의 값보다 작거나 같고, end 가 right_idx 의 값보다 작거나 같음
    if start <= points[left_idx] and end <= points[right_idx]:
        answer = right_idx - left_idx + 1

    # start 가 left_idx 의 값보다 크고, end 가 right_idx 의 값보다 작음
    elif start > points[left_idx] and end < points[right_idx]:
        answer = right_idx - left_idx - 1
    else:
        answer = right_idx - left_idx

    print(answer)
