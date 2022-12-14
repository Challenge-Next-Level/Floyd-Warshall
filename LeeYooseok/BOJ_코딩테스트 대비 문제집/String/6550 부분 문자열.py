import sys

input = sys.stdin.readline

while True:
    try:
        s, t = input().split()

        s_len = len(s)
        t_len = len(t)

        s_idx, t_idx = 0, 0

        while t_idx < t_len:
            if s_idx >= s_len:
                break
            if s[s_idx] == t[t_idx]:
                s_idx += 1
            t_idx += 1

        if s_idx >= s_len:
            print("Yes")
        else:
            print("No")
    except:
        exit()
