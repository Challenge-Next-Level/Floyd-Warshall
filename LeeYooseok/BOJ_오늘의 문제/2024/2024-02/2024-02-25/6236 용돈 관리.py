N, M = map(int, input().split())
plan_list = list()
for _ in range(N):
    plan_list.append(int(input()))

left = min(plan_list)
right = sum(plan_list)

answer = 0
while left <= right:
    mid = (left + right) // 2

    money = mid # 현재 가진 동
    num = 1 # 인출 횟수
    for i in range(N):
        # 가진 돈이 부족하면, 돈 다 집어넣고 다시 인출
        if money < plan_list[i]:
            money = mid
            num += 1
        money -= plan_list[i]

    # 인출 횟수가 M 보다 크거나, 인출한 금액이 하루를 다 살기에 부족한 경우
    if num > M or mid < max(plan_list):
        left = mid + 1
    else:
        right = mid - 1
        answer = mid

print(answer)