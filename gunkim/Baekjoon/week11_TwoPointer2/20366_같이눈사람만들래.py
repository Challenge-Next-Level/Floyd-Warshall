# 입력 값의 크기가 매우 큰것으로 착각하여 for 문 사용을 생각지도 않았다
# 첫 눈사람을 만들 수 있는 경우에 대한 모든 경우를 그저 투포인터로 따지면 됐다
# 추가로 python3는 시간초과가 발생한다. pypy3로 해야한다
import sys

N = int(sys.stdin.readline())
diameter = list(map(int, sys.stdin.readline().split()))
diameter.sort()

answer = float('inf')
for i in range(N - 1):
    for j in range(i + 1, N): # 눈사람 1을 만들 수 있는 모든 경우
        height = diameter[i] + diameter[j]
        # 눈사람 2를 만들 수 있는 모든 경우
        left, right = 0, N - 1
        while left < right:
            if left == i or left == j:
                left += 1
                continue
            if right == i or right == j:
                right -= 1
                continue
            snow_man = diameter[left] + diameter[right]
            if snow_man - height > 0:
                right -= 1
            else:
                left += 1
            answer = min(answer, abs(snow_man - height))

print(answer)