def solution(n, times):
    times.sort()
    left, right = 0, max(times) * n
    answer = 0

    def check(total_time):
        people_cnt = 0
        for time in times:
            people_cnt += (total_time // time)

        return people_cnt >= n

    while left <= right:
        mid = (left + right) // 2

        # mid 시간 안에 심사를 다 받을 수 있는지 확인
        if check(mid):
            answer = mid
            right = (mid - 1)
        else:
            left = (mid + 1)

    return answer
