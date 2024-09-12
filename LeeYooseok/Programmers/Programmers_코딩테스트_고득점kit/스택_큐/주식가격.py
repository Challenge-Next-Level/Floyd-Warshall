def solution(prices):
    answer = []
    length = len(prices)
    for i in range(0, length - 1):
        cnt = 0
        for j in range(i + 1, length):
            cnt += 1
            if prices[i] > prices[j]:
                break
        answer.append(cnt)
    answer.append(0)
    return answer