import sys


N, M = map(int, sys.stdin.readline().split()) # 입국 심사대, 친구 수
waiting = []
for _ in range(N): # 입국 심사대 마다 소요되는 시간
    waiting.append(int(sys.stdin.readline().split()[0]))
waiting.sort()

answer = float('inf')
left, right = waiting[0], M * waiting[-1]
while left <= right:
    checked_person = 0
    mid = (left + right) // 2 # 소요 시간을 fix 해준다
    for i in range(N):
        checked_person += mid // waiting[i] # 소요 시간 동안 각 심사대에서 심사할 수 있는 사람들의 수를 센다
    if checked_person < M:
        left = mid + 1
    else:
        right = mid - 1
        answer = mid
print(answer)
