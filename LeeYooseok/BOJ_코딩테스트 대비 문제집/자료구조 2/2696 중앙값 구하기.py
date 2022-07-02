import heapq

T = int(input())

for _ in range(T):
    M = int(input())

    num_list = list()
    for _ in range(int(M // 10) + 1):
        num_list.extend(list(map(int, input().split())))

    result = list()
    h = list()
    heapq.heappush(h, num_list.pop(0))

    while True:
        tmp_num = list()

        for _ in range(int(len(h) // 2)):
            tmp_num.append(heapq.heappop(h))

        mid_num = heapq.heappop(h)
        result.append(mid_num)

        heapq.heappush(h, mid_num)
        for n in tmp_num:
            heapq.heappush(h, n)

        if num_list:
            heapq.heappush(h, num_list.pop(0))
            heapq.heappush(h, num_list.pop(0))
        else:
            break

    len_result = len(result)

    print(len_result)

    for i in range(int(len_result // 10) + 1):
        tmp_result = result[10 * i: 10 * (i + 1)]
        print(" ".join(list(map(str, tmp_result))))