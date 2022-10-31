# 차곡차곡 순서대로 구현을 하면 됐다. 크게 2가지 정도를 잘못 구현을 했었는데
# 1. 기존에 추천했던 후보를 추천할 때 시간 갱신을 모르고 해버렸다 -> 시간 갱신 하지 않게 수정
# 2. 투표수가 적고, 가장 오래된 후보를 찾을 때(mivVal, minTime) 잘못 구현했다 (예를 들어 minVal은 갱신하는데 minTime은 갱신안함)
import sys

n = int(input())
m = int(input())
numbers = list(map(int, sys.stdin.readline().split()))
inf = float('inf')
answer = [[inf, inf] for _ in range(101)]
size = 0
time = 0

for num in numbers:
    time += 1
    if size < n: # 빈 액자가 있는 경우
        if answer[num] == [inf,inf]:
            size +=1
            answer[num] = [1,time]
        else:
            answer[num][0] += 1
    else: # 빈 액자가 없는 경우
        if answer[num] != [inf, inf]: # 기존 추천했던 후보를 추천한 경우
            answer[num][0] += 1 # 투표수만 증가
        else: # 추천되지 않은 후보를 추천한 경우
            minVal = inf
            minTime = inf
            minIdx = -1
            for i in range(1, 101): # 투표수가 가장 적고, 가장 오래전에 추천된 사람을 찾기
                if minVal > answer[i][0]:
                    minVal,minTime = answer[i]
                    minIdx = i
                elif minVal == answer[i][0]:
                    if minTime > answer[i][1]:
                        minVal,minTime = answer[i]
                        minIdx = i
            answer[minIdx] = [inf,inf]
            answer[num] = [1, time]

for i in range(1, 101):
    if answer[i] != [inf,inf]:
        print(i, end=' ')