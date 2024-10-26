N = int(input())
road_list = list(map(int, input().split()))  # raod_list[i] = i 번째 도시에서 i+1 번째 도시로 가는 도로의 길이
city_list = list(map(int, input().split()))  # city_list[i] = i 번째 도시의 기름값

answer = 0
min_price = city_list[0]

for i in range(N - 1):
    if min_price > city_list[i]:
        min_price = city_list[i]

    answer += (min_price * road_list[i])

print(answer)