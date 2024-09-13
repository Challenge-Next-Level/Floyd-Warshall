def solution(array, commands):
    answer = []

    for command in commands:
        i, j, k = command

        sub_array = array[i - 1:j]
        sub_array.sort()

        answer.append(sub_array[k - 1])

    return answer