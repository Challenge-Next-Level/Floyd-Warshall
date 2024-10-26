import sys

input = sys.stdin.readline

p, m = map(int, input().split())

room_list = list()

for _ in range(p):
    l, n = input().split()
    l = int(l)

    find_room = False
    for i in range(len(room_list)):
        level, started, player_list = room_list[i]

        if started:
            continue

        if level - 10 <= l <= level + 10:
            room_list[i][2].append([n, l])
            find_room = True

        if len(room_list[i][2]) == m:
            room_list[i][1] = True

        if find_room:
            break

    if not find_room:
        if m == 1:
            sd = True
        else:
            sd = False
        room_list.append([l, sd, [[n, l]]])

for l, s, p_list in room_list:
    if s:
        print("Started!")
    else:
        print("Waiting!")
    for p in sorted(p_list, key=lambda x: x[0]):
        print(*p[::-1])

