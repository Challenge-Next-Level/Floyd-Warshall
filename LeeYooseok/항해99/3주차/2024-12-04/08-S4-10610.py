N = list(input())

N.sort(reverse=True)

now_value = 0
zero = False
for n in N:
    if n != '0':
        now_value += int(n)
    else:
        zero = True
        break

if zero and (now_value % 3 == 0):
    print("".join(N))
else:
    print(-1)
