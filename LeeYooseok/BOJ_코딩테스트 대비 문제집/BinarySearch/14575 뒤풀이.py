import sys

N, T = map(int, input().split())

total_L = 0

people_list = list()
start, end = sys.maxsize, 0
for _ in range(N):
    L, R = map(int, input().split())
    people_list.append([L, R])

    total_L += L

    # 시작, 끝 : 최소 필요량, 최대 필요량
    start, end = min(start, L), max(end, R)

# 모든 참가자들의 최소 필요량 합 > 구입한 술의 양 -> 불가능
if total_L > T:
    print(-1)
    exit()

answer = sys.maxsize

while start <= end:
    mid = (start + end) // 2

    # mid 를 넘지 않으면서, 합이 정확히 T가 되어야 함. -> 가능한 최소 양 <= T <= 가능한 최대 양 이면 가능한 것으로 확인
    # 또한 각 사람의 술 양은 p[0] <= * <= p[1] 이어야 함.
    isPossible = True
    minSum, maxSum = 0, 0
    for p in people_list:
        if p[0] <= mid:
            minSum += p[0]
            maxSum += min(mid, p[1])  # 최대 mid 를 넘으면 안돼기 때문에, min 사용
        else:
            isPossible = False
    if isPossible and (minSum <= T <= maxSum):
        answer = min(answer, mid)
        end = mid - 1
    else:
        start = mid + 1

if answer == sys.maxsize:
    print(-1)
else:
    print(answer)
