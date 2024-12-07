N = int(input())
K = int(input())
sensor_loc_list = list(map(int, input().split()))

if K >= N:
    print(0)
    exit()

sensor_loc_list.sort()
distance_list = list()
for i in range(1, N):
    distance_list.append(sensor_loc_list[i] - sensor_loc_list[i - 1])

distance_list.sort(reverse=True)
for _ in range(K - 1):
    distance_list.pop(0)

print(sum(distance_list))