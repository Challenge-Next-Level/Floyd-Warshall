import sys

input = sys.stdin.readline

N = int(input())
value_list = list(map(int, input().split()))

answer = [0, 0]
answer_value = sys.maxsize

left, right = 0, N - 1
while left < right:
    left_value, right_value = value_list[left], value_list[right]
    now_value = left_value + right_value

    if abs(now_value) < answer_value:
        answer = [left_value, right_value]
        answer_value = abs(now_value)

        if answer_value == 0:
            break

    if now_value < 0:
        left += 1
    elif now_value > 0:
        right -= 1

print(*answer)