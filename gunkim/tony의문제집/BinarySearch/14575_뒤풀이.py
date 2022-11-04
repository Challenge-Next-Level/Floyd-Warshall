# 구하는 값이 사람당 만족하는 최소 주량을 넘는지 확인 필요
# 모두 술을 나눠주었을 때 소비해야하는 술(t)을 넘기는지 확인
# 애초에 술을 모두 소비할 수 없는 경우 예외 처리
import sys
n, t = map(int, sys.stdin.readline().split())
people = []
left, right = 1, 1
total_min = 0 # 사람당 만족하는 최소 주량을 더한다.
for _ in range(n):
    L, R = map(int, sys.stdin.readline().split())
    people.append([L, R])
    right = max(right, R)
    total_min += L

if t < total_min: # 소비해야 하는 술 보다 적다면 정답을 구할 수 없음
    print(-1)
else:
    answer = -1
    while left <= right:
        mid = (left + right) // 2
        total = 0
        count = 0
        for i in range(n):
            if people[i][0] > mid:
                continue
            count += 1
            if people[i][1] < mid: # 술찌인 사람
                total += people[i][1]
            else: # 여유 있는 사람
                total += mid
        if count != n or total < t: # 모두 만족을 못하거나 술을 모두 못 나눠 줌
            left = mid + 1
        else:
            right = mid - 1
            if answer != -1:
                answer = min(answer, mid)
            else:
                answer = mid

    print(answer)