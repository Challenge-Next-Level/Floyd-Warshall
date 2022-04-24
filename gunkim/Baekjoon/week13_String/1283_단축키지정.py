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
        if wl[0].upper() not in dict and flag == 0:  # 단축키가 없을 때
            word += '[' + wl[0] + ']' + wl[1:] + ' '
            dict[wl[0].upper()] = wl.upper()
            flag = 1
        else:
            word += wl + ' '
    if flag == 1: # 맨앞단어에서 단축키를 찾았을 때 출력 후 종료
        print(word)
        continue
    word = ''
    for wl in w_lst: # 앞선 단계에서 출력하지 못했으니 다음 단계에서 단축키를 찾는다
        for idx in range(len(wl)):
            if wl[idx].upper() not in dict and flag == 0: # 단축키가 없을 때
                word += '[' + wl[idx] + ']' + wl[idx + 1:]
                dict[wl[idx].upper()] = wl[idx:].upper()
                flag = 1
                break
            else:
                word += wl[idx]
        word += ' '
    print(word)