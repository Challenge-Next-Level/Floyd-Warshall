T = int(input())

for _ in range(T):
    f, s = map(str, input().split())
    len_f, len_s = len(f), len(s)
    if len_f < len_s:
        f = '0' * (len_s - len_f) + f
    else:
        s = '0' * (len_f - len_s) + s

    answer = ''
    s = s[::-1]
    f = f[::-1]


    idx = 0
    chk = False
    while idx < len(s) and idx < len(f):
        if s[idx] == '0' and f[idx] == '0':
            if chk:
                answer += '1'
            else:
                answer += '0'
            chk = False
        elif s[idx] == '1' and f[idx] == '1':
            if chk:
                answer += '1'
            else:
                answer += '0'
            chk = True
        else:
            if chk:
                answer += '0'
                chk = True
            else:
                answer += '1'
                chk = False

        idx += 1
    if chk:
        answer += '1'

    print(int(answer[::-1]))


