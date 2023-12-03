N = int(input())

answer_list = [N]


def check(num_list):
    global answer_list
    next_num = num_list[-2] - num_list[-1]

    if next_num >= 0:
        temp_num_list = num_list[:]
        temp_num_list.append(next_num)
        check(temp_num_list)
    else:
        if len(answer_list) <= len(num_list):
            answer_list = num_list


for i in range(1, N + 1):
    check([N, i])

print(len(answer_list))
print(*answer_list)