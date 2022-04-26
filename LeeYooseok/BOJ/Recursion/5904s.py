n = int(input())

# i번째 수열까지 만들면 됨
i = 0
j = 3
old, new = 0, 0

while True:
    new = old + j + old
    old = new
    j += 1

    if new > n:
        break

    i += 1


# 몇번째, 인덱스, 문자열 길이
def moo(t, idx, length):
    if t == 0:
        if idx == 0:
            print("m")
        else:
            print("o")
        return

    # 가운데 : [(length - (t + 3) ) // 2 : (length - (t + 3) ) // 2 + (t + 3)]
    if (length - (t + 3)) // 2 <= idx < (length - (t + 3)) // 2 + (t + 3):
        now_idx = idx - (length - (t + 3)) // 2
        moo(0, now_idx, 0)
    # 오른쪽 : [(length - (t + 3) ) // 2 + (t + 3) : ]
    elif idx >= (length - (t + 3)) // 2 + (t + 3):
        now_idx = idx - (length - (t + 3)) // 2 - (t + 3)
        moo(t - 1, now_idx, (length - (t + 3)) // 2)
    # 왼쪽 : [ : (length - (t + 3) ) // 2]
    else:
        moo(t - 1, idx, (length - (t + 3)) // 2)


moo(i, n - 1, new)
