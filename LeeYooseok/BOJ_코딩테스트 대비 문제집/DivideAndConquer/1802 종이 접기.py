# 가운데 숫자와  왼쪽, 오른쪽 부분이 반대이어야 한다.??

def solve(_num_list, _n):
    global chk
    if _n == 1:
        return
    mid_idx = _n // 2
    left_num_list, right_num_list = _num_list[:mid_idx], _num_list[mid_idx + 1:]

    # 가능
    right_num_list.reverse()
    for idx in range(mid_idx):
        if left_num_list[idx] == right_num_list[idx]:
            chk = False
            return

    if chk:
        solve(left_num_list, mid_idx)
        solve(right_num_list, mid_idx)


T = int(input())
for _ in range(T):
    in_out_list = list(input()) # 0 : IN, 1 : OUT

    n = len(in_out_list)

    if n == 1:
        print("YES")
    else:
        chk = True
        solve(in_out_list, n)

        if chk:
            print("YES")
        else:
            print("NO")




