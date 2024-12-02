N = int(input())
number_list = list(map(int, input().split()))
S = int(input())

for i in range(N):
    # 현재 위치부터 다음 S개까지 수들 중 최대값
    max_num = max(number_list[i: min(N, i + S + 1)])
    idx = number_list.index(max_num)

    # 교환 (max_num 을 i 위치로 갖고온다.)
    for j in range(idx, i, -1):
        number_list[j], number_list[j - 1] = number_list[j - 1], number_list[j]

    # 교환 횟수 만큼 S를 감소시켜준다.
    S -= (idx - i)
    if S <= 0:
        break

print(*number_list)