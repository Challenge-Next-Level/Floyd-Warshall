# 개인적으로 어려웠는데 아이디어가 번뜩 떠올라 풀어서 뿌듯한 문제
# 돌이 1개, 2개, 3개... 일 때 누가 이기는지 경우를 저장해가며 돌의 개수를 늘려간다
N = int(input())

if N == 1 or 3 <= N <= 4: # 1 ~ 4개 일때는 임의로 누가 이기는지 저장한다
    print('SK')
elif N == 2:
    print('CY')
else: # 5개 이상일 때 부터 앞의 케이스를 보고 승리 예측이 가능해짐.
    case = [None] * (N + 1)

    case[1] = 'SK'
    case[2] = 'CY'
    case[3] = 'SK'
    case[4] = 'SK'
    idx = 5
    while idx <= N:
        if case[idx - 1] == 'SK' and case[idx - 3] == 'SK' and case[idx - 4] == 'SK':
            case[idx] = 'CY'
        else:
            case[idx] = 'SK'
        idx += 1
    print(case[N])