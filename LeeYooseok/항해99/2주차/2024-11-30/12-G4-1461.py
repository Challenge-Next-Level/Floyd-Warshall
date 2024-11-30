import sys

input = sys.stdin.readline

N, M = map(int, input().split())
location_list = list(map(int, input().split()))
positive_list = list()
negative_list = list()

for location in location_list:
    if location > 0:
        positive_list.append(location)
    elif location < 0:
        negative_list.append(location)

distance = list()

negative_list.sort()
for i in range(len(negative_list) // M):
    distance.append(abs(negative_list[M * i]))
if len(negative_list) % M != 0:
    distance.append(abs(negative_list[(len(negative_list) // M) * M]))

positive_list.sort(reverse=True)
for i in range(len(positive_list) // M):
    distance.append(positive_list[M * i])
if len(positive_list) % M != 0:
    distance.append(positive_list[(len(positive_list) // M) * M])

distance.sort()
answer = distance.pop()
answer += 2 * sum(distance)
print(answer)