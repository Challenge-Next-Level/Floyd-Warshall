n, m = map(int, input().split())

lst = [[0] * n for _ in range(m)]
for y in range(m):
    for x in range(n):
        lst[y][x] = [y,x]

check = [[0] * n for _ in range(m)]

def combination(count, r, c):
    global ret  # 조합 갯수 세기
    if count == 3:

        return
    for i in range(r, n):
        if i == r:  # 해당 row일 때는 col보다 작은 값은 보지 않기
            c2 = c
        else:
            c2 = 0
        for j in range(c2, m):
            if check[j][i] == 0:
                check[j][i] = 1
                selected.append(lst[j][i])
                combination(count+1, j, i)
                check[j][i] = 0
                selected.pop()
ret = 0
selected = []

combination(0, 0, 0)
print(ret)