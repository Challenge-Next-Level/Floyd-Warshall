dance_list_list = list()
while True:
    try:
        dance_list = list(input().split())
    except:
        break
    if not dance_list:
        break
    dance_list_list.append(dance_list)

for dance_list in dance_list_list:
    dance_cnt = len(dance_list)
    dance_dict = {'dip': [], 'twirl': [], 'hop': [], 'jiggle': [], 'clap': [], 'stomp': []}

    for idx in range(dance_cnt):
        dance_dict[dance_list[idx]].append(idx)

    error_list = list()

    # 1. dip은 jiggle을 춘 다음이나 다다음, 또는 twirl을 추기 전에 출 수 있다. 예를 들면 다음과 같다.
    for dip_idx in dance_dict['dip']:
        chk = False
        if dip_idx > 0:
            if dance_list[dip_idx - 1] == 'jiggle':
                chk = True
            if dip_idx > 1:
                if dance_list[dip_idx - 2] == 'jiggle':
                    chk = True
        if chk:
            pass
        for twirl_idx in dance_dict['twirl']:
            if twirl_idx > dip_idx:
                chk = True
                break
        if not chk:
            error_list.append('1')
            break

    # 2. 모든 춤은 clap stomp clap으로 끝나야 한다.
    if not ((dance_cnt - 1) in dance_dict['clap'] and (dance_cnt - 2) in dance_dict['stomp'] and (dance_cnt - 3) in
            dance_dict['clap']):
        error_list.append('2')

    # 3. 만약 twirl을 췄다면, hop도 춰야한다.
    if dance_dict['twirl'] and not dance_dict['hop']:
        error_list.append('3')

    # 4. jiggle로 춤을 시작할 수 없다.
    if 0 in dance_dict['jiggle']:
        error_list.append('4')

    # 5. 반드시 dip을 춰야 한다.
    if len(dance_dict['dip']) == 0:
        error_list.append('5')

    if not error_list:
        print("from ok: ", end="")
    else:
        if len(error_list) >= 2:
            print("from errors ", end="")
            for error in error_list[:-2]:
                print(error, end=", ")
            print(error_list[-2] + " and " + error_list[-1], end=": ")
        else:
            print("from error ", end="")
            print(error_list[0], end=": ")
    print(*dance_list)
