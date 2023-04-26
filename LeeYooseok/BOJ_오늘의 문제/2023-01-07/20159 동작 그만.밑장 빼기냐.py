from collections import deque

N = int(input())
card_list = deque(list(map(int, input().split())))

answer = 0


def solve(temp_card_list, chk, total):
    global answer
    if len(temp_card_list) == 0:
        answer = max(total, answer)
        return

    if not chk:
        copy_card_list = deque([item for item in temp_card_list])
        temp_total = total + copy_card_list.pop()
        copy_card_list.popleft()
        solve(copy_card_list, True, temp_total)

    copy_card_list = deque([item for item in temp_card_list])
    temp_total = total + copy_card_list.popleft()
    copy_card_list.popleft()
    solve(copy_card_list, chk, temp_total)

solve(card_list, False, 0)

print(answer)