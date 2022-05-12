# 2 pointer 문제

import sys


def solution(queue1, queue2):
    answer = sys.maxsize
    sum_1, sum_2 = sum(queue1), sum(queue2)
    if sum_1 == sum_2:
        return 0
    total = sum_1 + sum_2
    total = int(total / 2)

    temp = queue1 + queue2
    interval_sum = 0
    end = 0
    n = len(temp)

    # start를 차례대로 증가시키며 반복
    for start in range(n):
        while interval_sum < total and end < n:
            interval_sum += temp[end]
            end += 1
        if interval_sum == total:
            ofs = 0
            # start가 두번재 queue에 있을 경우
            if start + 1 > int(n // 2):
                # 두번째 queue에 있는 start앞의 것을 한번 더 옮겨줌
                ofs += (start + 1 - int(n // 2))
            # end가 첫번째 queue에 있을 경우
            if end < int(n // 2):
                # 첫번재 queue에 있는 start 앞의 것을 한번 더 옮겨줌
                ofs += start
            result = start + (n - end - 1) + ofs
            answer = min(answer, result)
        interval_sum -= temp[start]

    temp = queue2 + queue1
    interval_sum = 0
    end = 0


    # start를 차례대로 증가시키며 반복
    for start in range(n):
        # end를 가능한 만큼 이동시키기
        while interval_sum < total and end < n:
            interval_sum += temp[end]
            end += 1
        # 부분합이 m일 때 카운트 증가
        if interval_sum == total:
            ofs = 0
            if start + 1 > int(n // 2):
                ofs += (start + 1 - int(n // 2))
            if end < int(n // 2):
                ofs += start
            result = start + (n - end - 1) + ofs
            answer = min(answer, result)
        interval_sum -= temp[start]

    if answer == sys.maxsize:
        return -1
    else:
        return answer


print(solution([3, 2, 7, 2], [4, 6, 5, 1]))
print(solution([1, 2, 1, 2], [1, 10, 1, 2]))
print(solution([1, 1], [1, 5]))
