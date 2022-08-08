# 통과
def solution(levels):
    problem = len(levels) * 0.25
    answer = -1
    levels.sort(reverse=True)
    temp = levels[:int(problem)]
    if len(temp) > 0:
        return temp[-1]
    else:
        return answer

print(solution([1,2,3,4]))