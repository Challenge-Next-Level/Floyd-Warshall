import heapq

def solution(operations):
    num_list = list()

    for operation in operations:
        operation = operation.split(" ")
        if operation[0] == "I":
            heapq.heappush(num_list, int(operation[1]))
        elif num_list:
            if operation[1] == "1":
                num_list.remove(max(num_list))
                heapq.heapify(num_list)
            else:
                heapq.heappop(num_list)

    if not num_list:
        return [0, 0]
    return [max(num_list), min(num_list)]