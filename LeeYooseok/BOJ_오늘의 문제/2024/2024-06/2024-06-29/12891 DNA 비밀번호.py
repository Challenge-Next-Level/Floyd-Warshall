from collections import defaultdict

S, P = map(int, input().split())
DNA_str = input()
min_cnt_list = list(map(int, input().split()))  # 부분문자열에 포함되어야 할 {‘A’, ‘C’, ‘G’, ‘T’} 의 최소 개수

# 현재 부분문자열에 포함되어 있는 {‘A’, ‘C’, ‘G’, ‘T’} 의 개수
now_cnt_dict = defaultdict(int)
for idx in range(P):
    s = DNA_str[idx]
    now_cnt_dict[s] += 1

answer = 0


def check():
    global answer
    check_char_list = ["A", "C", "G", "T"]
    check_flag = True
    for char_idx in range(4):
        if now_cnt_dict[check_char_list[char_idx]] < min_cnt_list[char_idx]:
            check_flag = False
            break
    if check_flag:
        answer += 1


for idx in range(S - P + 1):
    if idx > 0:
        now_cnt_dict[DNA_str[idx - 1]] -= 1
        now_cnt_dict[DNA_str[P + idx - 1]] += 1
    check()
print(answer)
