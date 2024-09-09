def solution(edges):
    # edges의 요소를 순회하면서 각 노드별로 들어오는 간선과 나가는 간선의 개수를 표시한다.
    def count_edges(edges):
        edge_counts = dict()
        for a, b in edges:
            if not edge_counts.get(a):
                edge_counts[a] = [0, 0]
            if not edge_counts.get(b):
                edge_counts[b] = [0, 0]

            # output edge와 input edge의 개수를 추가
            edge_counts[a][0] += 1 # a는 n번 노드에서 나가는 간선
            edge_counts[b][1] += 1 # b는 n번 노드로 들어오는 간선
        return edge_counts

    # 각 노드별 간선들의 수를 확인하여 조건에 맞는 노드의 개수를 answer에 추가한다.
    # '생성된 정점'은 나가는 간선의 수가 2 이상이고, 들어오는 간선의 수가 0이다.
    # '막대 모양 그래프'의 수는 나가는 간선의 수가 0, 들어오는 간선의 수가 1인 노드의 개수와 같다.
    # '8자 모양 그래프'의 수는 나가는 간선의 수가 2, 들어오는 간선의 수도 2인 노드의 개수와 같다.
    # '도넛 모양 그래프'는 '생성된 정점'의 나가는 간선의 수에서 막대 모양 그래프와 8자 모양 그래프의 개수를 빼서 구한다.

    def check_answer(edge_counts):
        answer = [0, 0, 0, 0]
        for key, counts in edge_counts.items():
            # 생성된 정점
            if counts[0] >= 2 and counts[1] == 0:
                answer[0] = key
            # 막대 모양 그래프
            elif counts[0] == 0 and counts[1] > 0:
                answer[2] += 1
            # 8자 모양 그래프
            elif counts[0] >= 2 and counts[1] >= 2:
                answer[3] += 1

        # 도넌 모양 그래프의 수 확인
        answer[1] = (edge_counts[answer[0]][0] - answer[2] - answer[3])
        return answer

    edge_counts = count_edges(edges)
    return check_answer(edge_counts)