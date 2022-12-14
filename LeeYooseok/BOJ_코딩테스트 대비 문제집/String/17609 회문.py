import sys

input = sys.stdin.readline

T = int(input())


def check(s_idx, e_idx):
    while s_idx < e_idx:
        if text[s_idx] == text[e_idx]:
            s_idx += 1
            e_idx -= 1
        else:
            if s_idx < e_idx - 1:
                temp = text[:e_idx] + text[e_idx + 1:]
                if temp[:] == temp[::-1]:
                    return 1
            if s_idx + 1 < e_idx:
                temp = text[:s_idx] + text[s_idx + 1:]
                if temp[:] == temp[::-1]:
                    return 1
            return 2
    return 0

for _ in range(T):
    text = input().strip()
    t_len = len(text)

    print(check(0, t_len - 1))