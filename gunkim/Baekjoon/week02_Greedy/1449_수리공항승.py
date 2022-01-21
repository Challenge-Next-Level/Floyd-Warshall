import sys

N, L = map(int, sys.stdin.readline().split())
leak = list(map(int, sys.stdin.readline().split()))
leak.sort() # 누수 위치를 정렬
visit = [0] * N # 테이프를 붙인 곳인지 체크
count = 0 # 테이프 갯수
for i in range(N):
    if visit[i] == 0:
        visit[i] = 1
        count += 1
        j = i + 1
        while j < N and leak[j] - leak[i] < L: # 누수 위치의 간격이 L보다 작으면 하나의 테이프로 두 곳 모두 붙일 수 있음
            visit[j] = 1
            j += 1
print(count)