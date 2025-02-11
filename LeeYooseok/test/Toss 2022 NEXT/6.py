# 통과 - 만보기
# 1, 2, 3 단계 합쳐서 만보기 걸음 횟수가 많은 순서대로 이름 출력
# 각 단계에서 같은 이름 나오면 더 많이 걸은 횟수로 취급
# 최종 단계에서 걸음 횟수가 같으면 사전순으로 출력
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
