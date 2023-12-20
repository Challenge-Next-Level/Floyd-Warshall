N = int(input())

node_list = [list(map(int, input().split())) for _ in range(N)]
for n in range(N):
    node_list[n].append(n)

# 비용, A 노드, B 노드
edge_list = list()
# for a_node in range(N):
#     a_x, a_y, a_z = node_list[a_node]
#     for b_node in range(a_node + 1, N):
#         b_x, b_y, b_z = node_list[b_node]
#         min_cost = min(abs(a_x - b_x), abs(a_y - b_y), abs(a_z - b_z))
#         edge_list.append([min_cost, a_node, b_node])

node_list.sort(key=lambda x: x[0])
for i in range(N - 1):
    cost = abs(node_list[i][0] - node_list[i + 1][0])
    edge_list.append([cost, node_list[i][3], node_list[i + 1][3]])

node_list.sort(key=lambda x: x[1])
for i in range(N - 1):
    cost = abs(node_list[i][1] - node_list[i + 1][1])
    edge_list.append([cost, node_list[i][3], node_list[i + 1][3]])

node_list.sort(key=lambda x: x[2])
for i in range(N - 1):
    cost = abs(node_list[i][2] - node_list[i + 1][2])
    edge_list.append([cost, node_list[i][3], node_list[i + 1][3]])

edge_list.sort()

# union find 함수를 통한 최소 신장 트리
parent_node = [i for i in range(N)]
rank = [1 for _ in range(N)]


def find(node):
    if node != parent_node[node]:
        parent_node[node] = find(parent_node[node])
    return parent_node[node]


answer = 0
for c, a, b in edge_list:
    a_parent = find(a)
    b_parent = find(b)

    if a_parent != b_parent:
        if a_parent > b_parent:
            parent_node[a_parent] = b_parent
        else:
            parent_node[b_parent] = a_parent

        answer += c

print(answer)
