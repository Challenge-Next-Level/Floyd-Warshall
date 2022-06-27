import sys

input = sys.stdin.readline

N = int(input())

problem_dict = dict()

for _ in range(N):
    P, L = map(int, input().split())
    if L in problem_dict.keys():
        problem_dict[L].append(P)
    else:
        problem_dict[L] = [P]

M = int(input())

cmd_list_list = list()
for _ in range(M):
    cmd_list = list(input().split())
    cmd_list_list.append(cmd_list)

for cmd_list in cmd_list_list:
    cmd = cmd_list[0]

    if cmd == 'add':
        if int(cmd_list[2]) in problem_dict.keys():
            problem_dict[int(cmd_list[2])].append(int(cmd_list[1]))
        else:
            problem_dict[int(cmd_list[2])] = [int(cmd_list[1])]
    elif cmd == 'solved':
        for k in problem_dict.keys():
            if int(cmd_list[1]) in problem_dict[k]:
                if len(problem_dict[k]) == 1:
                    problem_dict.pop(k)
                else:
                    problem_dict[k].remove(int(cmd_list[1]))
                break
    elif cmd == 'recommend':
        if cmd_list[1] == '1':
            _max = max(problem_dict.keys())
            if len(problem_dict[_max]) == 1:
                print(problem_dict[_max][0])
            else:
                print(max(problem_dict[_max]))
        elif cmd_list[1] == '-1':
            _min = min(problem_dict.keys())
            if len(problem_dict[_min]) == 1:
                print(problem_dict[_min][0])
            else:
                print(min(problem_dict[_min]))
