import heapq

n = int(input())
lecture_list = []
for i in range(n):
    lecture_list.append(list(map(int, input().split())))

lecture_list.sort(key=lambda x: (x[1]))

p_list = []
for i in lecture_list:
    heapq.heappush(p_list, i[0])
    if len(p_list) > i[1]:
        heapq.heappop(p_list)

print(sum(p_list))
