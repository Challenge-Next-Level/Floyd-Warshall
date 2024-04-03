import sys
from collections import deque

input = sys.stdin.readline

# 1000 ~ 9999 사이의 소수 구하기
n = 10000
a = [False, False] + [True] * (n - 1)
primes = []

for i in range(2, n + 1):
    if a[i]:
        if i >= 1000:
            primes.append(str(i))
        for j in range(2 * i, n + 1, i):
            a[j] = False
primes_cnt = len(primes)

def bfs(num, target):
    visited = [False for _ in range(primes_cnt)]
    num_idx = primes.index(num)
    visited[num_idx] = True
    queue = deque([[num, num_idx, 0]])

    while queue:
        now_num, now_num_idx, cnt = queue.popleft()

        if now_num == target:
            return cnt

        for next_idx in range(primes_cnt):
            if visited[next_idx]:
                continue

            next_num = primes[next_idx]
            diff_cnt = 0
            for k in range(4):
                if now_num[k] != next_num[k]:
                    diff_cnt += 1

            if diff_cnt == 1:
                visited[next_idx] = True
                queue.append([next_num, next_idx, cnt + 1])

    return -1

T = int(input())

for _ in range(T):
    num1, num2 = input().split()

    answer = bfs(num1, num2)

    if answer == -1:
        print("Impossible")
    else:
        print(answer)
