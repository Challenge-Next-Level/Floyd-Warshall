import sys

input = sys.stdin.readline

n = int(input())

cross_list = list(map(int, input().split()))
left_list = list(map(int, input().split()))
right_list = list(map(int, input().split()))

for i in range(n - 2):
    left_list[i + 1] += left_list[i]
    right_list[n - i - 3] += right_list[n - i - 2]

left_list.insert(0, 0)
right_list.append(0)

answer = [0, cross_list[0] + right_list[0]]

for i in range(n):
    # i + 1 번째에서 횡단보도 이용
    now_cost = left_list[i] + cross_list[i] + right_list[i]

    if now_cost < answer[1]:
        answer[0] = i + 1
        answer[1] = now_cost

print(" ".join(map(str, answer)))
