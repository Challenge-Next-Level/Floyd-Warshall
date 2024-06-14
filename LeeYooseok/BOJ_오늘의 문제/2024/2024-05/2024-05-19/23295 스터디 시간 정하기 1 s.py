import sys

input = sys.stdin.readline

N, T = map(int, input().split())

time_table = [0 for _ in range(100001)]

for _ in range(N):
    K = int(input())
    for _ in range(K):
        S, E = map(int, input().split())
        time_table[S] += 1  # S 시간에 한명 추가
        time_table[E] -= 1  # E 시간에 한명 빼기

# 부분합 -> 각 시간에 몇명이 스터디가 가능한지 확인
for i in range(1, 100001):
    time_table[i] += time_table[i - 1]

score = 0
for j in range(T):
    score += time_table[j]
max_score = score
start_time = 0

for k in range(1, 100001 - T):
    score -= time_table[k - 1]
    score += time_table[k + T - 1]

    if score > max_score:
        max_score = score
        start_time = k

print(start_time, start_time + T)