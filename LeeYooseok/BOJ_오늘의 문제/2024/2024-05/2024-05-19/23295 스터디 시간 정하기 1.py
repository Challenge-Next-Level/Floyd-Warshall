import sys

input = sys.stdin.readline

N, T = map(int, input().split())

time_table = [0 for _ in range(100001)]

for _ in range(N):
    K = int(input())
    for _ in range(K):
        S, E = map(int, input().split())
        for time in range(S, E):
            time_table[time] += 1

score = sum(time_table[0:T])
max_score = score
answer_start_time = 0
for start_time in range(100001 - T):
    score = score - time_table[start_time - 1] + time_table[start_time + T - 1]

    if score > max_score:
        max_score = score
        answer_start_time = start_time

print(answer_start_time, answer_start_time + T)
