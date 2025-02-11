# 통과
def solution(tasks):
    temp_dict = dict()
    for t in tasks:
        if t not in temp_dict.keys():
            temp_dict[t] = 1
        else:
            temp_dict[t] += 1

    answer = 0
    for v in temp_dict.values():
        if v == 1:
            answer = -1
            break
        else:
            answer += (v // 3)
            if v % 3 == 1:
                answer += 1 # -> 4원 : 2원 * 2 -3원 * 1
            elif v % 3 == 2:
                answer += 1 # -> 2원 : 2원 * 1

    return answer