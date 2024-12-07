N = int(input())

answer = 0
now_value = 0

while now_value < N:
    now_value = 2 ** answer
    answer += 1

print(answer)