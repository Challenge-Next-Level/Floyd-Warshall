import sys

N, M = map(int, sys.stdin.readline().split())
lecture = list(map(int, sys.stdin.readline().split()))

left, right = max(lecture), sum(lecture)  # left값 설정 때문에 답이 결정됨. 0으로 두면 x
# 이유는 이것! left를 0으로 지정하면 M개의 블루레이를 만족하는 크기가 어쩌다 나올 수 있게 되고 그때 크기는 마지막 강의가 말도 안되게 커도 허용할 수 있게됨.
while left <= right:
    mid = (left + right) // 2
    count, idx = 0, 0 # 블루레이 갯수, lecture의 index
    loc_sum = 0 # 각 블루레이의 강의 길이 합
    while idx < N:
        if loc_sum + lecture[idx] > mid:
            count += 1
            loc_sum = 0
        loc_sum += lecture[idx]
        if idx == N - 1:
            count += 1
        idx += 1
    if count > M:
        left = mid + 1
    else:
        right = mid - 1
print(left) # left가 최소 블루레이 갯수가 된다.