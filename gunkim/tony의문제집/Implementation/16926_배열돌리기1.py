import sys

n, m, r = map(int, sys.stdin.readline().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))


def switch(row, col, value):
    temp = arr[row][col]
    arr[row][col] = value
    return temp


for _ in range(r):
    for i in range(min(n, m) // 2):
        y, x = i, i
        prevVal = arr[y][x]

        # 좌(상하 이동)
        for j in range(i+1, n-i):
            y = j
            prevVal = switch(y, x, prevVal)
        # 하(좌우 이동)
        for j in range(i+1, m-i):
            x = j
            prevVal = switch(y, x, prevVal)
        # 우(하상 이동)
        for j in range(n-i-2, i-1, -1):
            y = j
            prevVal = switch(y, x, prevVal)
        # 상(우좌 이동)
        for j in range(m-i-2, i-1, -1):
            x = j
            prevVal = switch(y, x, prevVal)

for i in range(n):
    print(' '.join(map(str, arr[i])))