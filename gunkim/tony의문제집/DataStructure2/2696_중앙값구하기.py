# 코드 적기 전 로직 생각
# 1. 선형탐색을 하면서 숫자 추가
# 2. 중간 인덱스에 해당하는 값 출력
import sys

t = int(input())
for _ in range(t):
    # 입력 값 받기
    n = int(input())
    nums = []
    for _ in range(n // 10 + 1):
        nums += list(map(int, sys.stdin.readline().split()))

    sortedList = [] # 숫자들을 하나씩 추가할 리스트
    length = 0
    for i in range(n):
        num = nums[i]
        idx = -1
        for j in range(length): # 1. 선형탐색을 하면서 숫자 추가
            if num > sortedList[j]:
                idx = j
            else:
                break
        length += 1
        if idx == -1:
            sortedList = [num] + sortedList[:]
        else:
            sortedList = sortedList[:idx+1] + [num] + sortedList[idx+1:]
        # 출력하기
        if i == 0:
            print(n // 2 + 1)
        if i % 2 == 0:
            if (length + 1) % 20 == 0 or length == n:
                print(sortedList[i // 2], end='\n')
            else:
                print(sortedList[i // 2], end=' ')
