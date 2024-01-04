from collections import defaultdict

N, L = map(int, input().split())

traffic_light_dict = defaultdict(list)

for _ in range(N):
    D, R, G = map(int, input().split())

    traffic_light_dict[D] = [R, G]

answer = 1
now_loc = 1

while now_loc < L:
    if now_loc in traffic_light_dict.keys():
        # 현재 시간에 red 이면
        if (answer % sum(traffic_light_dict[now_loc])) <= traffic_light_dict[now_loc][0]:
            answer += (traffic_light_dict[now_loc][0] - answer % sum(traffic_light_dict[now_loc]))

    answer += 1
    now_loc += 1

print(answer)

