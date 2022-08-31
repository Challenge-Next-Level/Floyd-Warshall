import sys

n = input()

min_v = sys.maxsize
max_v = 0


# 홀수 카운트
def command1(n):
    odd_n = 0
    for i in n:
        if int(i) % 2 != 0:
            odd_n += 1
    return odd_n


def solve(n, odd_n):
    global max_v, min_v

    # 한자리수
    if len(n) == 1:
        min_v = min(min_v, odd_n)
        max_v = max(max_v, odd_n)
    # 두자리수
    elif len(n) == 2:
        temp = str(int(n[0]) + int(n[1]))
        solve(temp, odd_n + command1(temp))
    # 세자리수 이상
    else:
        # 이중 반복문을 이용해 세부분으로 나눈다.
        for i in range(len(n) - 2):
            for j in range(i + 1, len(n) - 1):
                a = n[:i + 1]
                b = n[i + 1: j + 1]
                c = n[j + 1:]
                temp = str(int(a) + int(b) + int(c))
                solve(temp, odd_n + command1(temp))


solve(n, command1(n))
print(min_v, max_v)
