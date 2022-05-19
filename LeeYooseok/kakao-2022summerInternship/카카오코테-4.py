import sys

gate_list = list()
summit_list = list()
result = sys.maxsize
result_summit = sys.maxsize


def dfs(summit, paths, cur, intensity):
    global result, result_summit
    if cur[-1] in summit_list:
        if cur[-1] == summit:
            if result > intensity:
                result = intensity
                result_summit = summit
            elif result == intensity:
                if result_summit > summit:
                    result_summit = summit
            return
    else:
        for path in paths:
            # in 메소드 시간 생각
            if path[0] == cur[-1] and path[1] not in gate_list and path[1] not in cur:
                dfs(summit, paths, cur + [path[1]], max(intensity, path[2]))


# 정상까지만 가장 적은 intensity 로 가면 됨
def solution(n, paths, gates, summits):
    global result, result_summit
    result = sys.maxsize
    result_summit = sys.maxsize

    temp = list()
    for path in paths:
        temp.append([path[1], path[0], path[2]])
    paths.extend(temp)

    global gate_list, road, visited, summit_list
    gate_list = gates
    summit_list = summits

    # pair <입구, 정상>
    for g in gates:
        for s in summits:
            dfs(s, paths, [g], 0)

    print(result_summit, result)


solution(6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1, 3], [5])
solution(7, [[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]], [1], [2, 3, 4])
solution(7, [[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]], [3, 7], [1, 5])
solution(5, [[1, 3, 10], [1, 4, 20], [2, 3, 4], [2, 4, 6], [3, 5, 20], [4, 5, 6]], [1, 2], [5])
