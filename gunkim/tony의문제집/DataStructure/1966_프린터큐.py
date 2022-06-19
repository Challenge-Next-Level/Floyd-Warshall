import sys
from collections import deque

t = int(input())
for _ in range(t):
    n, m = map(int, sys.stdin.readline().split()) # 종이 수, 찾고자 하는 종이의 인덱스
    important = deque(map(int, sys.stdin.readline().split())) # 종이 중요도
    check = deque() # 종이 중요도, 해당 종이가 찾고자 하는 것인지 체크
    for i in range(n):
        if i == m: # 해당 종이가 찾고자 하는 것인지 체크
            check.append([important[i], 1])
        else:
            check.append([important[i], 0])
    count = 1
    while check:
        num, isCheck = check.popleft()
        if num != max(list(important)): # 중요도 최상이 아니었다면 다시 DEQUEUE에 추가
            check.append([num, isCheck])
            important.append(num)
        else: # 중요도 최상이라면 종이 출력
            if isCheck == 1: # 찾고자 하는 종이었다면
                print(count)
                break
            else:
                count += 1
        important.popleft()