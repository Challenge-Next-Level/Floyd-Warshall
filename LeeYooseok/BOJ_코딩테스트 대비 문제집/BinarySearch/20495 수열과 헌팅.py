N = int(input())
num_array = list()
minus_list = list()
plus_list = list()
for _ in range(N):
    a, b = map(int, input().split())
    num_array.append([a - b, a + b])
    minus_list.append(a - b)
    plus_list.append(a + b)

# 정렬
minus_list.sort()
plus_list.sort()


def lower_bound(min_num):
    # a + b 를 다 모았을 때, a - b 보다 작거나 같은 수의 개수
    start, end = 0, N
    while start < end:
        mid = (start + end) // 2

        if plus_list[mid] >= min_num:
            end = mid
        else:
            start = mid + 1

    return end


def upper_bound(max_num):
    # a - b 를 다 모았을 때, a + b 보다 작거나 같은 수의 개수
    start, end = 0, N
    while start < end:
        mid = (start + end) // 2

        if minus_list[mid] <= max_num:
            start = mid + 1
        else:
            end = mid

    return end


for min_num, max_num in num_array:
    # a - b 가 올 수 있는 가장 빠른 위치 : a + b 를 다 모았을 때, a - b 보다 작거나 같은 수의 개수
    index_min = lower_bound(min_num)
    # a + b 가 올 수 있는 가장 느린 위치 : a - b 를 다 모았을 때, a + b 보다 작거나 같은 수의 개수
    index_max = upper_bound(max_num)

    print(index_min + 1, index_max)