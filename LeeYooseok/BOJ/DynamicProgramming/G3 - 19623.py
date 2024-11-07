import sys

input = sys.stdin.readline

N = int(input())
meeting_list = [[0, 0, 0]] + [list(map(int, input().split())) for _ in range(N)]

# dp[i] = i번째 회의까지 고려했을 시, 가능한 최대 인원 수
dp = [0 for _ in range(N + 1)]

# 종료 시간이 빠른 순으로 정렬
meeting_list.sort(key=lambda x: x[1])


# now_meeting 을 시작할 수 있는 회의들 중, 가장 최근 시작된 회의
def binary_search(now_meeting_idx, start_time):
    left, right = 0, now_meeting_idx - 1
    possible_meeting_idx = 0

    while left <= right:
        mid = (left + right) // 2

        if meeting_list[mid][1] <= start_time:
            possible_meeting_idx = mid
            left = mid + 1
        else:
            right = mid - 1

    return possible_meeting_idx


dp[1] = meeting_list[1][2]

answer = 0

for i in range(2, N + 1):
    now_meeting = meeting_list[i]

    # i번째 회의를 진행할 수 있는 경우들 중 인원 수를 최대로 하는 회의의 index -> 가장 최근 시작된 회의
    k = binary_search(i, now_meeting[0])

    # i번째 회의를 진행할 수 있는 경우들 중 최댓값 + i번째 회의의 인원 수, i번째 회의를 진행 안하는 경우
    dp[i] = max(dp[k] + now_meeting[2], dp[i - 1])

print(dp[N])
