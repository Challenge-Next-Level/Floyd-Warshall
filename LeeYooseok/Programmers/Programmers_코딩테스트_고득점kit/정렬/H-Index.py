def solution(citations):
    answer = 0

    citations.sort()

    for i in range(len(citations)):
        h_index = len(citations) - i
        if citations[i] >= h_index:
            answer = h_index
            break

    return answer