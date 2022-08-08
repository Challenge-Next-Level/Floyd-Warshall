# 통과
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
        return int(str(answer[i]) * 3)

print(solution('111999333'))