S = input()
len_s = len(S)

alpha_dict = dict()

for s in S:
    if s in alpha_dict.keys():
        alpha_dict[s] += 1
    else:
        alpha_dict[s] = 1

def backTracking(pre, cnt):
    answer = 0
    if cnt == len_s:
        answer += 1

    for k in alpha_dict.keys():
        # 현재 단어가 이전 단어일 경우와 현재 단어의 개수가 0일 경우 다음 단어를 확인한다.
        if k == pre or alpha_dict[k] == 0:
            continue

        alpha_dict[k] -= 1  # 현재 단어의 개수를 감소
        answer += backTracking(k, cnt + 1)  # 백트래킹 후 리턴 받은 수를 answer에 더한다.
        alpha_dict[k] += 1  # 현재 단어의 개수를 증가

        # answer 리턴
    return answer


print(backTracking('', 0))
