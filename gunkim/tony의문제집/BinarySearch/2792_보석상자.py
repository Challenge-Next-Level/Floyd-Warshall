# 이분탐색은 어떻게 푸는 거였더라? 하는 감각이 사라지면 엄청 어려운 문제이다
# 하지만 다시 또 감각을 익히게 되면 구현하는데 큰 어려움은 없다,,,근데 진짜 어렵네 오랜만에 보니까
import sys

n, m = map(int, input().split())
jewel = []
for i in range(m):
    size = list(map(int, sys.stdin.readline().split()))[0]
    jewel.append(size)
answer = float('inf')


left, right = 1, max(jewel)
while left <= right:
    mid = (left+right)//2
    person = 0 # 몇 명에게 나눠줄 것인가
    for i in range(m):
        person += jewel[i]//mid # 몫 만큼 나눠준다
        if jewel[i]%mid != 0: # 나머지가 있다면 한 명 더 나눠줄 수 있음
            person += 1
    if person > n:
        left = mid + 1
    else:
        right = mid - 1
        answer = min(answer, mid)
print(answer)