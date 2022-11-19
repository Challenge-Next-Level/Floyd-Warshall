N = int(input())

num_array = list()
decreasing_num_set = set()


def dfs():
    if len(num_array) != 0:
        decreasing_num_set.add(int("".join(map(str, num_array))))

    for i in range(0, 10):
        if len(num_array) == 0 or num_array[-1] > i:  # 마지막 값이 더 큰 경우
            num_array.append(i)
            dfs()
            num_array.pop()


try:
    dfs()
    decreasing_num_set = list(decreasing_num_set)
    decreasing_num_set.sort()
    print(decreasing_num_set[N - 1])
except:
    print(-1)
