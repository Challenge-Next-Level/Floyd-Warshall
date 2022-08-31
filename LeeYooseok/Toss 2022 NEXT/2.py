# 통과 - 문제 난이도 상위 25% 문제들 중 쉬운 문제 출력
def solution(levels):
    problem = len(levels) * 0.25
    answer = -1
    levels.sort(reverse=True)
    temp = levels[:int(problem)]
    if len(temp) > 0:
        return temp[-1] # 내림 차순 정렬이므로 마지막에 해당하는 부분이 가장 쉬운 문제
    else:
        return answer

print(solution([1,2,3,4]))