import heapq

N = int(input())


def time_to_number(time):
    time_list = time.split(":")
    HH = time_list[0]
    MM = time_list[1]
    SS, sss = time_list[2].split(".")

    return int(HH + MM + SS + sss)


bus_list = list()

for _ in range(N):
    in_time, out_time = input().split()
    in_time = time_to_number(in_time)
    out_time = time_to_number(out_time)

    bus_list.append([in_time, out_time])

bus_list.sort()

min_heap = list()
# 가장 빨리 들어오는 버스의 [나가는 시각, 들어오는 시각]
heapq.heappush(min_heap, [bus_list[0][1], bus_list[0][0]])
answer = 1

for i in range(1, N):
    now_bus = bus_list[i]

    # 현재 가장 빨리 나가는 버스
    fast_out_bus = min_heap[0]

    # 현재 버스가 현재 가장 빨리 나가는 버스의 나가는 시각보다 더 빨리 들어온다면
    if now_bus[0] < fast_out_bus[0]:
        # 종점에 같이 있어야 함
        answer += 1
        heapq.heappush(min_heap, [now_bus[1], now_bus[0]])
    # 현재 버스가 현재 가장 빨리 나가는 버스의 나가는 시각보다 더 늦게 들어온다면
    else:
        # 가장 빨리 나가는 버스는 나간다.
        heapq.heappop(min_heap)
        # 현재 버스만 종점에 들어감
        heapq.heappush(min_heap, [now_bus[1], now_bus[0]])

print(answer)
