import sys

input = sys.stdin.readline

N, K, Q, M = map(int, input().split())

sleep_list = [0] * (N + 3) # 졸고있는 학생 체크
chk_list = [0] * (N + 3) # 출석 체크

# 졸고있는 학생 체크
for idx in list(map(int, input().split())):
    sleep_list[idx] = 1

# 출석 체크
for idx in list(map(int, input().split())):
    if sleep_list[idx] == 1:
        continue

    for i in range(idx, N + 3, idx):
        if sleep_list[i] != 1:
            chk_list[i] = 1

# 출석체크 한 사람들 부분합
prefix_sum_list = [chk_list[0]]
for i in range(1, N+3):
    prefix_sum_list.append(prefix_sum_list[-1] + chk_list[i])

# M번 확인
for _ in range(M):
    S, E = map(int, input().split()) # S ~ E 까지 출석체크 안한 사람들 수
    # = 전체 사람 수 - 출석 체크 한 사람 수
    answer = (E - S + 1) - (prefix_sum_list[E] - prefix_sum_list[S - 1])
    print(answer)



