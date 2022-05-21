import sys

n, m, k = map(int, sys.stdin.readline().split())
A = [] # 각 칸에 추가되는 양분의 양
for _ in range(n):
    A.append(list(map(int, sys.stdin.readline().split())))
trees = [[[] for _ in range(n)] for _ in range(n)] # 3차 리스트 만드는 방법 (중요!)
for _ in range(m):
    x, y, z = map(int, sys.stdin.readline().split())
    trees[x - 1][y - 1].append(z)

dir = [[-1,-1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1,-1], [1,0], [1,1]]
drink = [[5] * n for _ in range(n)] # 내가 읽지 못했던 조건 1 (초기 양분은 모두 5이다)

for i in range(k):
    for b in range(n):
        for a in range(n):
            trees[b][a].sort()
            length = len(trees[b][a])
            for t in range(length):
                if trees[b][a][t] <= drink[b][a]: # 봄
                    drink[b][a] -= trees[b][a][t]
                    trees[b][a][t] += 1 # 내가 읽지 못했던 조건 2 (나무의 나이는 무조건 1 증가이다)
                else: # 여름
                    for idx in range(t, length):
                        drink[b][a] += trees[b][a].pop() // 2
                    break
    for b in range(n):
        for a in range(n):
            for t in trees[b][a]:
                if t % 5 == 0: # 가을
                    for dy, dx in dir:
                        ny, nx = b + dy, a + dx
                        if 0 <= ny < n and 0 <= nx < n:
                            trees[ny][nx].append(1)
            drink[b][a] += A[b][a] # 겨울

answer = 0
for i in range(n):
    for j in range(n):
        answer += len(trees[i][j])
print(answer)