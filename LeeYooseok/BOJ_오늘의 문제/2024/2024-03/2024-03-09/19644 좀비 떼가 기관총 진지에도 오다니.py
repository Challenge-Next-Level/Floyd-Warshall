import sys
from collections import deque

input = sys.stdin.readline

L = int(input())

M_L, M_K = map(int, input().split())

C = int(input())

zombie_list = [int(input()) for _ in range(L)]

que = deque()
# 현재 사용한 수류탄 개수
now_cnt = 0

# 기관총 범위 내부에 있는 놈들
for i in range(min(M_L, L)):
    # 기관총으로 죽는다면,
    if zombie_list[i] - M_K * (i + 1 - now_cnt) <= 0:
        # M_K * (i + 1 - cnt) -> i + 1 - cnt 번 기관총을 맞는다.
        que.append(0)
    else:
        que.append(zombie_list[i] - M_K * (i + 1 - now_cnt))
        now_cnt += 1
        C -= 1

    if C < 0:
        print("NO")
        exit()

# 기관총 범위 외부에 있는 놈들
for i in range(M_L, L):
    if que[0] > 0:
        # 수류탄 사용
        now_cnt -= 1
    que.popleft()
    if zombie_list[i] - M_K * (M_L - now_cnt) <= 0:
        que.append(0)
    else:
        que.append(zombie_list[i] - M_K * (M_L - now_cnt))
        now_cnt += 1
        C -= 1

    if C < 0:
        print("NO")
        exit()

print("YES")