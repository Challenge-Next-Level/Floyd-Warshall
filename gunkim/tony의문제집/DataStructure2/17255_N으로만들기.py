# 전 날에는 생각이 나지 않았는데 오늘 보고 바로 풀이가 생각이 났다.
N = input()


def check(number):
    if len(number) == 1: # 길이가 1이 되었다면 한 가지 경우 완성
        return 1
    flag = 0
    for i in range(len(number) - 1): # 숫자가 하나의 수로 되어있는지 확인
        if number[i] != number[i + 1]:
            flag = 1
            break
    if flag == 1: # 서로 다른 수 라면 앞,뒤를 각각 뺀 경우로 check
        return check(number[:-1]) + check(number[1:])
    else: # 하나의 수로 되어있는 경우 한 가지 경우 밖에 되지 않음
        return 1


print(check(N))