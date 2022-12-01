# python3는 시간초과 발생, pypy3로 채점
# 김밥을 모두 폐기할 수 있는 상황에 max(kimbab)을 할 경우 ValueError 발생, 예외처리를 함
import sys

n, k, m = map(int, sys.stdin.readline().split())
kimbab = []
for _ in range(n):
    kb = int(sys.stdin.readline().split()[0])
    if kb <= k:
        continue
    elif kb < 2*k:
        kb -= k
    else:
        kb -= 2*k
    kimbab.append(kb)

answer = -1
if len(kimbab) == 0:
    print(answer)
else:
    left, right = 1, max(kimbab)
    length = len(kimbab)
    while left <= right:
        mid = (left+right)//2
        total = 0
        for i in range(length):
            total += kimbab[i]//mid
        if total < m:
            right = mid - 1
        else:
            left = mid + 1
            answer = max(answer, mid)
    print(answer)