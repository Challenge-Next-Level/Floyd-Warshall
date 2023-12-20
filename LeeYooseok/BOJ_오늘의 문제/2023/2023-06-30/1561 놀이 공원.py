N, M = map(int, input().split())

time_list = list(map(int, input().split()))

if N <= M:
    print(N)
    exit()

start = 1
end = max(time_list) * N
minute = max(time_list) * N

while start < end:
    mid = (start + end) // 2

    # mid 시간안에 몇명의 아이들이 놀이기구를 탈 수 있는지
    temp = 0
    for i in range(M):
        temp += ((mid // time_list[i]) + 1)

    if temp < N:
        start = mid + 1
    else:
        minute = min(minute, mid)
        end = mid

# minute - 1 까지 몇명의 아이들이 탈 수 있는지 계산
temp = 0
for i in range(M):
    temp += (((minute - 1) // time_list[i]) + 1)

# minute 에 탈 수 있는 놀이기구 확인
for i in range(M):
    if minute % time_list[i] == 0:
        temp += 1
    if temp == N:
        print(i + 1)
        exit()