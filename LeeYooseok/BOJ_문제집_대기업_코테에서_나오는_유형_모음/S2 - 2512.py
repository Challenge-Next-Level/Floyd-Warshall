import sys

input = sys.stdin.readline

N = int(input())
request_money_list = list(map(int, input().split()))
limit_money = int(input())

if sum(request_money_list) <= limit_money:
    print(max(request_money_list))
else:
    # min(request_money_list) 조차도 배정을 못 받을 수 있기 때문에 -> left = 0
    left, right = 0, max(request_money_list)
    answer = left
    while left <= right:
        mid = (left + right) // 2

        total_money = 0
        for request_money in request_money_list:
            total_money += min(request_money, mid)

        if total_money <= limit_money:
            left = mid + 1
            answer = mid
        else:
            right = mid - 1

    print(answer)