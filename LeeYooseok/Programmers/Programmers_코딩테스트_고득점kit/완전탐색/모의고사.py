def solution(answers):
    a_answer = [1, 2, 3, 4, 5]
    b_answer = [2, 1, 2, 3, 2, 4, 2, 5]
    c_answer = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    score = {1: 0, 2: 0, 3: 0}

    for idx in range(len(answers)):
        if answers[idx] == a_answer[idx % 5]:
            score[1] += 1

        if answers[idx] == b_answer[idx % 8]:
            score[2] += 1

        if answers[idx] == c_answer[idx % 10]:
            score[3] += 1

    max_score = max(score.values())
    answer = list()
    for i in range(1, 4):
        if score[i] == max_score:
            answer.append(i)

    return answer
