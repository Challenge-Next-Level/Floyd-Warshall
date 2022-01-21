import sys

N, K = map(int, sys.stdin.readline().split())
table = sys.stdin.readline()
eat = [0] * N # 햄버거가 먹혔는지 체크
count = 0 # 몇 명이 먹었는지 체크
for i in range(N):
    if table[i] == 'P':
        for j in range(i - K, i + K + 1): # 범위 안에 있는 햄버거 탐색
            if 0 <= j < N and table[j] == 'H' and eat[j] == 0:
                count += 1
                eat[j] = 1
                break
print(count)