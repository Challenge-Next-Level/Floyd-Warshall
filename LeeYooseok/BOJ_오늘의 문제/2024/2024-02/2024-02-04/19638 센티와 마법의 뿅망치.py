import heapq

N, H, T = map(int, input().split())

people_list = list()
for _ in range(N):
    heapq.heappush(people_list, -1 * int(input()))

answer = 0
while answer < T:
    now_people = -1 * heapq.heappop(people_list)

    if now_people >= H:
        answer += 1
        if now_people == 1:
            heapq.heappush(people_list, -1)
        else:
            heapq.heappush(people_list, -1 * (now_people // 2))
    else:
        heapq.heappush(people_list, -1 * now_people)
        break

max_people = -1 * heapq.heappop(people_list)

if max_people >= H:
    print("NO")
    print(max_people)
else:
    print("YES")
    print(answer)