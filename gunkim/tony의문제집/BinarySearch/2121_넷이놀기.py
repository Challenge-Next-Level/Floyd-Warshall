# 솔직히 누가봐도 완전 탐색 같은데 알고리즘 분류가 이분 탐색으로 되어 있어서 황당했다
# 머리 속으로는 도저히 이해가 안가 다른 분들의 코드를 봤지만 단순한 완전 탐색일 뿐이었다,,, 허망
import sys

n = int(input())
length, height = map(int, input().split())
dot = set()
for _ in range(n):
    dot.add(tuple(map(int, sys.stdin.readline().split())))
dotList = list(dot)
answer = 0
for i in range(n):
    x, y = dotList[i]
    if (x+length,y) in dot and (x,y+height) in dot and (x+length, y+height) in dot:
        answer += 1
print(answer)