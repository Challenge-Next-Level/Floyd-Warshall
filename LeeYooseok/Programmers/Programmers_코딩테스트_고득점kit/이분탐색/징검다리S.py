def solution(distance, rocks, n):
    answer = 0

    rocks.append(distance)
    rocks = sorted(rocks)

    left, right = 0, distance

    while left <= right:

        # mid = n개의 돌을 제거했으 때, 남아있는 돌들의 거리 중 최소값 (?) -> 최대로 만들어야 함.
        mid = (left + right) // 2
        min_distance = float('inf')
        current = 0
        remove_cnt = 0

        for rock in rocks:
            diff = rock - current
            # 거리가 mid 보다 작다면, 해당 부분을 없애 줘야 함 -> 크게 만들어주기 위해서
            if diff < mid:
                remove_cnt += 1
            # 거리가 mid 보다 크다면, 해당 부분 유지 및 최소 거리 memorize
            else:
                current = rock
                min_distance = min(min_distance, diff)

        if remove_cnt > n:
            right = mid - 1
        else:
            answer = min_distance
            left = mid + 1

    return answer