# 틀렸음. 그래도 이전 내 풀이가 크게 개념을 벗어나진 않았음.
# 주요 포인트
# 1. 각 R에 대하여 왼쪽, 오른쪽에 K가 총 몇개 있는지 파악하는 것(난 K, R, K, R,... 순으로 몇개씩 연달아 있는지 파악함)
# 2. 맨 왼쪽, 오른쪽 R을 left, right로 지정후 투포인터 탐색(애초에 1번에서 자료를 투포인터를 활용할 수 없게 만들어서 완전탐색을 해버림)
import sys

s = sys.stdin.readline().strip()

lk = []
cnt = 0 # 내 왼쪽에 K가 몇 개 있냐
for i in s:
    if i == 'K':
        cnt += 1
    else:
        lk.append(cnt)

rk = [] # 내 오른쪽에 K가 몇 개 있냐
cnt = 0
for i in s[::-1]:
    if i == 'K':
        cnt += 1
    else:
        rk.append(cnt)
rk.reverse()

# lk, rk는 결국 R의 갯수만큼 크기가 됨.
l, r = 0, len(lk) - 1
ans = 0
while l <= r:
    ans = max(ans, r - l + 1 + 2 * min(lk[l], rk[r])) # (r - l + 1)은 R의 갯수를 의미.
    if lk[l] < rk[r]:
        l += 1
    else:
        r -= 1
print(ans)
