t = int(input())


def bs(target):
    # μ΄λΆ νμ
    start, end = 0, len(nums1)-1
    while start <= end:
        mid = (start + end) // 2
        now = nums1[mid]
        if now == target:
            print(1)
            return
        elif now > target:
            end = mid - 1
        else:
            start = mid + 1
    print(0)


for _ in range(t):
    n = int(input())
    nums1 = sorted(list(map(int, input().split())))
    m = int(input())
    nums2 = list(map(int, input().split()))

    for i in nums2:
        bs(i)


