# 딕셔너리로 푸니 당연히 시간초과가 뜬다.
# 최소, 최대 힙을 사용하도록 해보자.

import sys

input = sys.stdin.readline

N = int(input())


group_dict = dict()
level_dict = dict()

for _ in range(N):
    P, L, G = map(int, input().split())

    if G in group_dict.keys():
        group_dict[G].append([L, P])
    else:
        group_dict[G] = [[L, P]]

    if L in level_dict.keys():
        level_dict[L].append([P, G])
    else:
        level_dict[L] = [[P, G]]

M = int(input())

for _ in range(M):
    cmd_list = list(input().split())
    cmd = cmd_list[0]

    if cmd == 'add':
        P, L, G = map(int, cmd_list[1:])

        if G in group_dict.keys():
            group_dict[G].append([L, P])
        else:
            group_dict[G] = [[L, P]]

        if L in level_dict.keys():
            level_dict[L].append([P, G])
        else:
            level_dict[L] = [[P, G]]

    elif cmd == 'solved':
        P = int(cmd_list[1])
        find_G = False
        for k, v in level_dict.items():
            for idx in range(len(v)):
                p, g = v[idx][0], v[idx][1]
                if p == P:
                    target_g = g
                    find_G = True
                    if len(v) == 1:
                        level_dict.pop(k)
                    else:
                        v.pop(idx)
                    break
            if find_G:
                break

        for idx in range(len(group_dict[target_g])):
            l, p = group_dict[target_g][idx][0], group_dict[target_g][idx][1]

            if p == P:
                if len(group_dict[target_g]) == 1:
                    group_dict.pop(target_g)
                else:
                    group_dict[target_g].pop(idx)
                break
    elif cmd == 'recommend':
        G, x = map(int, cmd_list[1:])

        if x == -1:
            print(sorted(group_dict[G])[0][1])
        else:
            print(sorted(group_dict[G], reverse=True)[0][1])
    elif cmd == 'recommend2':
        x = int(cmd_list[1])

        if x == -1:
            print(sorted(level_dict[sorted(level_dict.keys())[0]])[0][0])
        else:
            print(sorted(level_dict[sorted(level_dict.keys(), reverse=True)[0]], reverse=True)[0][0])
    elif cmd == 'recommend3':
        x, L = map(int, cmd_list[1:])

        find_flag = False

        if x == 1:
            for l in list(sorted(level_dict.keys())):
                if l >= L:
                    print(sorted(level_dict[l])[0][0])
                    find_flag = True
                    break
        else:
            for l in list(sorted(level_dict.keys(), reverse=True)):
                if l <= L:
                    print(sorted(level_dict[l], reverse=True)[0][0])
                    find_flag = True
                    break

        if not find_flag:
            print(-1)