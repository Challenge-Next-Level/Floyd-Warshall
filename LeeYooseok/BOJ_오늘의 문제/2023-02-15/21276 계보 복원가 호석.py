from collections import deque

N = int(input())
name_list = list(input().split())

edge_dict = {name: [] for name in name_list}
indegree_dict = {name: 0 for name in name_list}

# 결과
root_list = list()
child_dict = {name: [] for name in name_list}

M = int(input())
for _ in range(M):
    A, B = input().split()
    edge_dict[B].append(A)
    indegree_dict[A] += 1

queue = deque()
# 조상을 큐에 넣는다.
for name, indegree in indegree_dict.items():
    if indegree == 0:
        queue.append(name)
        root_list.append(name)

while queue:
    now_node = queue.popleft()
    for next_node in edge_dict[now_node]:
        indegree_dict[next_node] -= 1
        if indegree_dict[next_node] == 0:
            queue.append(next_node)
            child_dict[now_node].append(next_node)

print(len(root_list))
print(*sorted(root_list))

for name in sorted(name_list):
    result = name + " " + str(len(child_dict[name]))
    if len(child_dict[name]) != 0:
        result += (" " + " ".join(sorted(child_dict[name])))
    print(result)

