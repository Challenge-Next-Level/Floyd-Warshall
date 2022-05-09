# 2 pointer 문제

import sys

def solution(queue1, queue2):
    answer = sys.maxsize
    sum_1, sum_2 = sum(queue1), sum(queue2)
    if sum_1 == sum_2:
        return 0
    total = sum_1 + sum_2
    total /= 2

    temp = queue1 + queue2
    interval_sum = 0
    end = 0
    n = len(temp)

    # start를 차례대로 증가시키며 반복
    for start in range(n):
        # end를 가능한 만큼 이동시키기
        while interval_sum < total and end < n:
            interval_sum += temp[end]
            end += 1
        # 부분합이 m일 때 카운트 증가
        if interval_sum == total:

            answer = min(answer, )


    temp = queue2 + queue1

    return answer

solution([3, 2, 7, 2],[4, 6, 5, 1])