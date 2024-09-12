def solution(arr):
    num_list = [-1]
    for num in arr:
        if num_list[-1] != num:
            num_list.append(num)

    return num_list[1:]