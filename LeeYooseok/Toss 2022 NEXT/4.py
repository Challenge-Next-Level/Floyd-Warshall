# 제출 못함 (아쉬움)
# 내가 초대한 사람 * 10 + 내가 초대한 사람이 초대한 사람 * 3 + 내가 초대한 사람이 초대한 사람이 초대한 사람
# 점수 순 -> 마지막으로 초대한 순 : 내림차순 3명 출력
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
    answer = sorted(score.items(), key=lambda x: (x[1][1], x[1][0]), reverse=True)
    t = list()
    for a in answer[:3]:
        t.append(a[0])
    return t

print(solution(
    [
        [1, 2],
        [2, 3],
        [2, 4],
        [2, 5],
        [5, 6],
        [5, 7],
        [6, 8],
        [2, 9],

    ]
))

class Node:
    def __init__(self, parent, idx=None):
        self.score = 0
        self.parent = parent

        if idx:
            self.idx = idx
        else:
            self.idx = -1


def new_solution(invitationPairs):
    node_dict = dict()
    for idx in range(len(invitationPairs)):
        pair = invitationPairs[idx]

        if pair[0] not in node_dict.keys():
            node_dict[pair[0]] = Node(None, idx)
        else:
            node_dict[pair[0]].idx = idx

        if pair[1] not in node_dict.keys():
            node_dict[pair[1]] = Node(node_dict[pair[0]])

        node_child = node_dict[pair[1]]

        node_child.parent.score += 10

        if node_child.parent.parent is not None:
            node_child.parent.parent.score += 3

            if node_child.parent.parent.parent is not None:
                node_child.parent.parent.parent.score += 1

    answer = sorted(node_dict.items(), key=lambda x: (x[1].score, x[1].idx), reverse=True)
    t = list()
    for a in answer[:3]:
        t.append(a[0])
    return t


print(new_solution([
    [1, 2],
    [2, 3],
    [2, 4],
    [2, 5],
    [5, 6],
    [5, 7],
    [6, 8],
    [2, 9],

]))


