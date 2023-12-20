from collections import defaultdict

N = int(input())
chk = list(input())
answer = 0

def solve(idx_list, n):
    global able
    if able:
        return
    if n == len(chk):
        # 오름차순인지 확인
        diff = idx_list[1] - idx_list[0]
        # 1부터 마지막 - 1 까지
        for chk_idx in range(1, n - 1):
            if idx_list[chk_idx + 1] - idx_list[chk_idx] != diff:
                return
        able = True
        return
    now_idx = idx_list[-1]
    for next_idx in chk_dict[chk[n]]:
        if now_idx < next_idx:
            copy_list = idx_list[:]
            copy_list.append(next_idx)
            solve(copy_list, n + 1)

for _ in range(N):
    able = False
    text = input()
    chk_dict = defaultdict(list)
    for idx in range(len(text)):
        if text[idx] in chk:
            chk_dict[text[idx]].append(idx)

    for start_idx in chk_dict[chk[0]]:
        solve([start_idx], 1)

    if able:
        answer += 1

print(answer)
