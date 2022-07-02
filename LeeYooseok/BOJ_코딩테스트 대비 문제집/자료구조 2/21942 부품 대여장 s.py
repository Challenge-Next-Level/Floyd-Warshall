# 분으로 계산하여 사용
import datetime as dt

N, L, F = input().split()

_d, _t = L.split("/")
_h, _m = map(int, _t.split(":"))
L = int(_d) * 24 * 60 + _h * 60 + _m

# key : 사람 이름, value : [[대여 장비 이름, 대여 날짜 및 시간]]
part_info = dict()

result_dict = dict()

for _ in range(int(N)):
    _date, _time, P, M = input().split()

    _date_time = dt.datetime.strptime(_date + " " + _time, "%Y-%m-%d %H:%M") - dt.datetime(2020, 12, 31)
    _min = int(_date_time.total_seconds() / 60)

    if M in part_info.keys():
        part_list = [item[1] for item in part_info[M]]
        flag = False
        for idx in range(len(part_list)):
            if part_list[idx] == P:
                diff_min = _min - part_info[M][idx][0] - L

                if diff_min > 0:
                    if M in result_dict.keys():
                        result_dict[M] += diff_min * int(F)
                    else:
                        result_dict[M] = diff_min * int(F)
                if len(part_info[M]) == 1:
                    part_info.pop(M)
                else:
                    part_info[M].pop(idx)
                flag = True
                break
        if not flag:
            part_info[M].append([_min, P])
    else:
        part_info[M] = [[_min, P]]

if result_dict:
    for k, v in sorted(result_dict.items()):
        print(k, v)
else:
    print(-1)
