"""
문자열을 만들어주니, 메모리 초과가 뜬다.
"""
import psutil

n = int(input())


def moo(t):
    if t == 0:
        return "moo"
    else:
        result = moo(t - 1) + "moo" + ("o" * t) + moo(t - 1)
        return result


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

real_result = moo(i)

print(real_result[n - 1])