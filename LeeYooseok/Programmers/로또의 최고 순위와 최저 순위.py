def solution(lottos, win_nums):
    zero = 0
    correct = 0
    for l in lottos:
        for w in win_nums:
            if l == 0:
                zero += 1
                break
            elif l == w:
                correct += 1
                break

    result = []

    if correct + zero == 6:
        result.append(1)
    elif correct + zero == 5:
        result.append(2)
    elif correct + zero == 4:
        result.append(3)
    elif correct + zero == 3:
        result.append(4)
    elif correct + zero == 2:
        result.append(5)
    elif correct + zero <= 1:
        result.append(6)

    if correct == 6:
        result.append(1)
    elif correct == 5:
        result.append(2)
    elif correct == 4:
        result.append(3)
    elif correct == 3:
        result.append(4)
    elif correct == 2:
        result.append(5)
    elif correct <= 1:
        result.append(6)

    return result


solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19])
solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25])
solution([45, 4, 35, 20, 3, 9],	[20, 9, 3, 45, 4, 35])
