T = int(input())

for _ in range(T):
    p = input()
    n = int(input())
    input_list = input()
    if n > 1:
        input_list = input_list[1:-1]
        input_list = input_list.split(",")
    elif n == 1:
        input_list = [input_list[1:-1]]
    else:
        input_list = []

    reverse = False
    flag = True
    for cmd in p:
        if cmd == 'R':
            reverse = not reverse
        elif cmd == 'D':
            if input_list:
                if reverse:
                    input_list.pop()
                else:
                    input_list.pop(0)
            else:
                print('error')
                flag = False
                break

    if flag:
        if reverse:
            input_list.reverse()
        print('[', end="")
        print(','.join(input_list), end="")
        print(']')