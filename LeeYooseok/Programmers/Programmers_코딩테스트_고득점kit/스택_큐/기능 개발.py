import math

def solution(progresses, speeds):
    deploy_list = list()
    answer = list()
    for idx in range(len(progresses)):
        remain_days = math.ceil((100 - progresses[idx]) / speeds[idx])
        if not deploy_list:
            deploy_list.append(remain_days)
            answer.append(1)

        else:
            if deploy_list[-1] >= remain_days:
                answer[-1] += 1
            else:
                deploy_list.append(remain_days)
                answer.append(1)
    return answer
