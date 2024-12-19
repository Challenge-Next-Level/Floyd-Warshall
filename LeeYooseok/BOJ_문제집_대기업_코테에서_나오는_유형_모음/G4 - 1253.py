N = int(input())
number_list = list(map(int, input().split()))

number_list.sort()

answer = 0

for i in range(N):
    number = number_list[i]
    left, right = 0, N - 1

    while left < right:
        now_value = number_list[left] + number_list[right]

        if now_value == number:
            if left == i:
                left += 1
            elif right == i:
                right -= 1
            else:
                answer += 1
                break
        elif now_value > number:
            right -= 1
        elif now_value < number:
            left += 1

print(answer)