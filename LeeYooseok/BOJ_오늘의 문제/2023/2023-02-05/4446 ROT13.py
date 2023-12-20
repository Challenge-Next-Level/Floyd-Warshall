moeum_list = ['a', 'i', 'y', 'e', 'o', 'u']
moeum_len = len(moeum_list)

zaeum_list = ['b', 'k', 'x', 'z', 'n', 'h', 'd', 'c', 'w', 'g', 'p', 'v', 'j', 'q', 't', 's', 'r', 'l', 'm', 'f']
zaeum_len = len(zaeum_list)

while True:
    try:
        text = list(input())
        answer = ''
        for t in text:
            isupper = False
            # 대문자
            if t.isupper():
                t = t.lower()
                isupper = True

            if t in moeum_list:
                t_idx = moeum_list.index(t)
                t = moeum_list[(t_idx + 3) % moeum_len]
            elif t in zaeum_list:
                t_idx = zaeum_list.index(t)
                t = zaeum_list[(t_idx + 10) % zaeum_len]

            if isupper:
                t = t.upper()
            answer += t
        print(answer)
    except :
        exit()
