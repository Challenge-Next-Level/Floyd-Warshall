# 사용량에 따른 요금 표
max_usage = 1000000
max_cost = 4979900
usage_to_cost = [2 * i for i in range(max_usage + 1)]
cost_to_usage = [0 for _ in range(max_cost + 1)]
for cost in range(0, 202, 2):
    cost_to_usage[cost] = (cost // 2)

for usage in range(101, 10001):
    usage_to_cost[usage] = usage_to_cost[usage - 1] + 3
    cost_to_usage[usage_to_cost[usage]] = usage
for usage in range(10001, max_usage + 1):
    usage_to_cost[usage] = usage_to_cost[usage - 1] + 5
    cost_to_usage[usage_to_cost[usage]] = usage


while True:
    A, B = map(int, input().split())

    if A == 0 and B == 0:
        break

    total_usage = 0
    if A > max_cost:
        total_usage += ((A - max_cost) // 7)
        A = max_cost
    total_usage += cost_to_usage[A]

    left, right = 0, total_usage

    while left <= right:
        mid = (left + right) // 2

        usage_a = mid
        usage_b = total_usage - usage_a

        cost_a = 0
        if usage_a > max_usage:
            cost_a += ((usage_a - max_usage) * 7)
            usage_a = max_usage
        cost_a += usage_to_cost[usage_a]

        cost_b = 0
        if usage_b > max_usage:
            cost_b += ((usage_b - max_usage) * 7)
            usage_b = max_usage
        cost_b += usage_to_cost[usage_b]

        if cost_b - cost_a == B:
            print(cost_a)
            break
        elif cost_b - cost_a > B:
            left = mid + 1
        else:
            right = mid - 1

