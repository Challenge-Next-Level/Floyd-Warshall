from collections import defaultdict, deque

N, M = map(int, input().split())


def structure():
    return [[], []]


graph = defaultdict(structure)

for _ in range(N + M):
    P, F, C = map(str, input().split())
    if C == '1':  # folder
        graph[P][0].append(F)
    else:
        graph[P][1].append(F)

Q = int(input())
for _ in range(Q):
    path_input = list(map(str, input().split("/")))
    path = deque([path_input[-1]])
    file_list = list()
    file_set = set()

    while path:
        now_folder = path.pop()
        for file in graph[now_folder][1]:
            file_list.append(file)
            file_set.add(file)

        for folder in graph[now_folder][0]:
            path.append(folder)

    print(len(file_set), len(file_list))