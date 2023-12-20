S = input()
s_tail = list()
for i in range(len(S)):
    s_tail.append(S[i:])

s_tail.sort()
for s in s_tail:
    print(s)