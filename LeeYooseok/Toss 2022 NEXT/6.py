# 통과
def solution(steps_one, names_one, steps_two, names_two, steps_three, names_three):
    one_dict = dict()
    for n, s in zip(names_one, steps_one):
        if n not in one_dict.keys():
            one_dict[n] = -1 * s
        else:
            one_dict[n] = min(one_dict[n], -1 * s)

    two_dict = dict()
    for n, s in zip(names_two, steps_two):
        if n not in two_dict.keys():
            two_dict[n] = -1 * s
        else:
            two_dict[n] = min(two_dict[n], -1 * s)

    three_dict = dict()
    for n, s in zip(names_three, steps_three):
        if n not in three_dict.keys():
            three_dict[n] = -1 * s
        else:
            three_dict[n] = min(three_dict[n], -1 * s)

    for k, v in two_dict.items():
        if k not in one_dict.keys():
            one_dict[k] = v
        else:
            one_dict[k] += v

    for k, v in three_dict.items():
        if k not in one_dict.keys():
            one_dict[k] = v
        else:
            one_dict[k] += v

    temp_list = sorted(one_dict.items(), key=lambda x: (x[1], x[0]))
    answer = []
    for t in temp_list:
        answer.append(t[0])
    return answer
