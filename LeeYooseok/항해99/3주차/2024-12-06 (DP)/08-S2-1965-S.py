import bisect

n = int(input())

box_size_list = list(map(int, input().split()))

LIS = [box_size_list[0]]

for i in range(1, n):
    now_box_size = box_size_list[i]

    if LIS[-1] < now_box_size:
        LIS.append(now_box_size)
    else:
        # LIS 인덱스에서 now_box_size 보다 크면서 가장 작은 값의 인덱스 반환
        insert_index = bisect.bisect_left(LIS, now_box_size)
        LIS[insert_index] = now_box_size

print(len(LIS))
