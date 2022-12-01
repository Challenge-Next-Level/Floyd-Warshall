# python3 는 시간초과 발생, pypy3 로 채점
n, m = map(int, input().split())

answer = 0


def dfs(y, x, nemo_list):
    global answer
    answer += 1
    for i in range(y, n):
        for j in range(m):
            if i == y and j <= x:
                continue
            nemo_list[i][j] = True
            if (0<=i-1<n and 0<=j-1<m and nemo_list[i-1][j-1]) and (0<=i-1<n and 0<=j<m and nemo_list[i-1][j]) and (0<=i<n and 0<=j-1<m and nemo_list[i][j-1]):
                nemo_list[i][j] = False
                continue
            dfs(i,j,nemo_list)
            nemo_list[i][j] = False
    return


for i in range(n):
    for j in range(m):
        nemo = [[False] * m for _ in range(n)]
        nemo[i][j] = True
        dfs(i, j, nemo)

print(answer+1)