# 여러 곳에서 막혔다... 에라토스테네스의 체를 재귀로 구현했지만 RecursionError가 발생

import sys

N = int(sys.stdin.readline())
save_idx = [0] * (N + 1)
save_idx[0] = save_idx[1] = 1

save = []
for i in range(2, N + 1):
    if save_idx[i] == 0:
        save.append(i)
        for j in range(i * 2, N + 1, i): # range에 3개 파라미터 사용, 알아두자
            save_idx[j] = 1

answer = 0
left, right = 0, 0
while right <= len(save):
    total = sum(save[left:right]) # sum으로 리스트의 합을 구한다
    if total == N:
        answer += 1
    if total <= N:
        right += 1
    else:
        left += 1
print(answer)
