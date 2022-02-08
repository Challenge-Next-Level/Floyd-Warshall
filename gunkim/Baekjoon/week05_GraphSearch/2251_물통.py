a, b, c = map(int, input().split()) # 물통의 용량

check = set([])


def dfs(x, y, z):
    case = [[x, y, z]]
    while case:
        nx, ny, nz = case.pop()
        nCase = ' '.join(map(str, [nx, ny, nz]))
        if nCase in check:
            continue
        check.add(nCase)
        sample = set([])
        if nx > 0:
            if ny < b:
                if nx >= b - ny:
                    sample.add(' '.join(map(str, [nx - (b - ny), b, nz])))
                else:
                    sample.add(' '.join(map(str, [0, nx + ny, nz])))
            if nz < c:
                if nx >= c - nz:
                    sample.add(' '.join(map(str, [nx - (c - nz), ny, c])))
                else:
                    sample.add(' '.join(map(str, [0, ny, nx + nz])))
        if ny > 0:
            if nx < a:
                if ny >= a - nx:
                    sample.add(' '.join(map(str, [a, ny - (a - nx), nz])))
                else:
                    sample.add(' '.join(map(str, [nx + ny, 0, nz])))
            if nz < c:
                if ny >= c - nz:
                    sample.add(' '.join(map(str, [nx, ny - (c - nz), c])))
                else:
                    sample.add(' '.join(map(str, [nx, 0, ny + nz])))
        if nz > 0:
            if nx < a:
                if nz >= a - nx:
                    sample.add(' '.join(map(str, [a, ny, nz - (a - nx)])))
                else:
                    sample.add(' '.join(map(str, [nx + nz, ny, 0])))
            if ny < b:
                if nz >= b - ny:
                    sample.add(' '.join(map(str, [nx, b, nz - (b - ny)])))
                else:
                    sample.add(' '.join(map(str, [nx, ny + nz, 0])))
        for i in sample:
            if i not in check:
                l, m, n = list(map(int, i.split()))
                case.append([l, m, n])
    return


dfs(0, 0, c) # 물통 (0, 0, c) 로 경우의 수 탐색
answer = []
for i in check:
    l, m, n = list(map(int, i.split()))
    if l == 0 and n not in answer:
        answer.append(n)
answer.sort()
print(' '.join(map(str, answer)))