A_form, B_form = input().split()

able_list = list()

for A in range(2, 37):
    for B in range(2, 37):
        try:
            num_A = int(A_form, A)
            num_B = int(B_form, B)

            if num_A == num_B and A != B and num_A >= 0:
                able_list.append([num_A, A, B])

        except:
            continue
if len(able_list) >= 2:
    print("Multiple")
elif len(able_list) == 0:
    print("Impossible")
else:
    print(*able_list[0])