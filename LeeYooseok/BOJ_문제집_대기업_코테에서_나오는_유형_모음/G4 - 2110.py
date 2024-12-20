N, C = map(int, input().split())
house_list = [int(input()) for _ in range(N)]
house_list.sort()

answer = 0
left, right = 1, house_list[-1] - house_list[0]

while left <= right:
    mid = (left + right) // 2

    now_house = house_list[0]
    count = 1
    for i in range(1, N):
        if house_list[i] >= now_house + mid:
            count += 1
            now_house = house_list[i]

    if count >= C:
        left = mid + 1
        answer = mid
    else:
        right = mid - 1

print(answer)