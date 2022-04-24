import sys

n = int(sys.stdin.readline())
words = []
for _ in range(n):
    words.append(sys.stdin.readline())

dict = {}
for w in words:
    w_lst = w.split(' ')
    w_lst[-1] = w_lst[-1].rstrip()

    flag = 0
    word = ''
    for wl in w_lst:
        if wl[0].upper() not in dict:  # 단축키가 없을 때
            word += '[' + wl[0] + ']' + wl[1:] + ' '
            dict[wl[0].upper()] = wl.upper()
            flag = 1
        else:
            word += wl
    if flag == 1:
        print(word)
        continue
    word = ''
    for wl in w_lst:
        for idx in range(len(wl)):
            if wl[idx].upper() not in dict:
                print('[', wl[idx], ']', wl[idx:], end='')
                dict[wl[idx].upper()] = wl[idx:].upper()
                flag = 1
                break

                print(wl[idx], end='')
                continue
            else:

        print(end=' ')
