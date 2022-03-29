import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
x = int(sys.stdin.readline())

answer = 0
a.sort() # 투 포인터의 핵심은 정렬이다!
left, right = 0, n - 1
while left < right:
    if a[left] + a[right] == x:
        answer += 1
    elif a[left] + a[right] < x:
        left += 1
        continue
    right -= 1
print(answer)