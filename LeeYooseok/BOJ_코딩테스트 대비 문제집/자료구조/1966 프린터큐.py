T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    priority = list(map(int, input().split()))

    _priority = list()
    for idx in range(len(priority)):
        _priority.append([priority[idx], idx, 0])

    cnt = 1
    while _priority:
        now_p = _priority.pop(0)
        flag = True
        for p in _priority:
            if p[0] > now_p[0]:
                flag = False
                break

        if flag:
            if now_p[1] == M:
                print(cnt)
                break
            cnt += 1
        else:
            _priority.append(now_p)

