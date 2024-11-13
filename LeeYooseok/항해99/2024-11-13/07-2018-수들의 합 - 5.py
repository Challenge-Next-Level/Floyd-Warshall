N = int(input())

num_list = [i for i in range(1, N + 1)]

left, right = 0, 0
answer = 0

while right < N + 1:
    now_value = sum(num_list[left:right])

    if now_value == N:
        answer += 1
        right += 1
    elif now_value < N:
        right += 1
    else:
        left += 1

print(answer)