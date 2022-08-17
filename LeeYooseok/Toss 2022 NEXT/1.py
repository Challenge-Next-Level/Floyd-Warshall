# 통과 - 주어진 문자열에서 숫자 3개 이어질때 그 수들 중 가장 큰 수 출력
def solution(s):
    answer = -1
    for i in range(len(s)-2):
        if s[i] == s[i+1] and s[i] == s[i+2]:
            answer = max(int(s[i]), answer)
    if answer == 0:
        return answer
    elif answer == -1:
        return answer
    else:
        return int(str(answer) * 3)

def solution_new(s):
    answer = -1
    idx = 0
    while idx < len(s) - 2:
        if s[idx] == s[idx + 1] and s[idx] == s[idx+2]:
            answer = max(int(s[idx]), answer)
            idx += 2
        else:
            idx += 1
    if answer == 0:
        return answer
    elif answer == -1:
        return answer
    else:
        return int(str(answer) * 3)


print(solution_new('111999333'))