# python datetime 사용 시, value error 또는 시간 초과

import datetime as dt

N, L, F = input().split()
_d, _t = L.split("/")
L = dt.datetime.strptime(str(int(_d) + 1) + " " + _t, "%d %H:%M")
L = L - dt.datetime(1900, 1, 1)

# key : 사람 이름, value : [[대여 장비 이름, 대여 날짜 및 시간]]
part_info = dict()

result = False

for _ in range(int(N)):
    _date, _time, P, M = input().split()

    _date_time = dt.datetime.strptime(_date + " " + _time, "%Y-%m-%d %H:%M")

    if M in part_info.keys():
        part_list = [item[1] for item in part_info[M]]
        flag = False
        for idx in range(len(part_list)):
            if part_list[idx] == P:
                td = _date_time - part_info[M][idx][0]
                # 벌금 계산
                _min = int((td - L).total_seconds() / 60)

                if _min > 0:
                    result = True
                    print(M, _min * int(F))

                flag = True
                break
        if not flag:
            part_info[M].append([_date_time, P])
    else:
        part_info[M] = [[_date_time, P]]

if not result:
    print(-1)

