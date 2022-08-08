# 제출 못함 (아쉬움)
def solution(invitationPairs):
    graph = dict()
    score = dict()
    for idx in range(len(invitationPairs)):
        p, t = invitationPairs[idx][0], invitationPairs[idx][1]
        if p not in graph.keys():
            graph[p] = [t]
            score[p] = [idx, [1]]
        else:
            graph[p].append(t)
            score[p] = [idx, [score[p][0] + 1]]

    for p in graph.keys():
        score_2, score_3 = 0, 0
        for p2 in graph[p]:
            if p2 in graph.keys():
                for p3 in graph[p2]:
                    if p3 in graph.keys():
                        score_3 += score[p3][1][0]
                score_2 += score[p2][1][0]

        score[p][1].append(score_2)
        score[p][1].append(score_3)

    for p in score.keys():
        s1, s2, s3 = score[p][1]
        score[p][1] = s1 * 10 + s2 * 3 + s3

    answer = sorted(score.items(), key = lambda x : (x[1][1], x[1][0]), reverse=True)
    t = list()
    for a in answer[:3]:
        t.append(a[0])
    return t

print(solution(
    [
        [1,2],
        [2,3],
        [2,4],
        [2,5],
        [5,6],
        [5,7],
        [6,8],
        [2,9],

    ]
))