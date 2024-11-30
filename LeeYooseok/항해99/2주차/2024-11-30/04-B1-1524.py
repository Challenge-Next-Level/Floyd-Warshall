T = int(input())
for _ in range(T):
    input()

    N, M = input().split()

    N_power_list = list(map(int, input().split()))
    M_power_list = list(map(int, input().split()))

    N_power_list.sort()
    M_power_list.sort()

    while N_power_list and M_power_list:
        if N_power_list[0] < M_power_list[0]:
            N_power_list.pop(0)
        else:
            M_power_list.pop(0)

    if N_power_list:
        print("S")
    else:
        print("B")