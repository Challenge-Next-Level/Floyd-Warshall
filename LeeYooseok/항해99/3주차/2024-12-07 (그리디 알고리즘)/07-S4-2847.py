import sys

input = sys.stdin.readline

N = int(input())

number_list = [int(input()) for _ in range(N)]

answer = 0
for i in range(N - 1, 0, -1):
    now_number = number_list[i]
    prior_number = number_list[i - 1]
    if now_number <= prior_number:
        answer += (prior_number - now_number) + 1
        number_list[i - 1] = now_number - 1

print(answer)