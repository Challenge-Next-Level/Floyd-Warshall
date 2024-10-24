# https://school.programmers.co.kr/learn/courses/30/lessons/92341
import math
# 어떤 차량이 입차된 후에 출차된 내역이 없다면, 23:59에 출차된 것으로 간주
# 차량 번호가 작은 자동차부터 청구할 주차 요금을 차례대로 정수 배열에 담아서 return

from collections import defaultdict

def solution(fees, records):
    base_min, base_cost, unit_min, unit_cost = fees

    car_dict = defaultdict(list)

    for record in records:
        time, car_number, in_or_out = record.split()

        hour, min = map(int, time.split(":"))
        min += (hour * 60)

        car_dict[car_number].append([min, in_or_out])

    answer = []

    for car_number in sorted(car_dict.keys()):
        parking_history_list = car_dict[car_number]
        total_min = 0
        for i in range(0, len(parking_history_list), 2):
            in_min = parking_history_list[i][0]

            if (len(parking_history_list) % 2 != 0) and (i == len(parking_history_list) - 1):
                out_min = 23*60 + 59
            else:
                out_min = parking_history_list[i + 1][0]

            total_min += (out_min - in_min)

        cost = 0

        if total_min >= base_min:
            total_min -= base_min
            cost += (math.ceil(total_min / unit_min) * unit_cost)

        cost += base_cost
        answer.append(cost)

    return answer