from itertools import combinations

while True:
    num_list = list(map(int, input().split()))

    k = num_list[0]
    if k == 0:
        exit()
    S = num_list[1:]

    for comb in combinations(S, 6):
        print(*comb)

    print()