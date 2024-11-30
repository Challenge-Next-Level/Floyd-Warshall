import sys

input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split()))

num_list.sort()

answer = 0
for i in range(N):
    num = num_list[i]
    left, right = 0, len(num_list) - 1
    while left < right:
        # 숫자를 만들 수 있다면,
        if num_list[left] + num_list[right] == num:
            # 왼쪽 수가 현재 목표 숫자라면
            if left == i:
                left += 1
            # 오른쪽 수가 현재 목표 숫자라면
            elif right == i:
                right -= 1
            else:
                answer += 1
                break
        elif num_list[left] + num_list[right] > num:
            right -= 1
        elif num_list[left] + num_list[right] < num:
            left += 1

print(answer)