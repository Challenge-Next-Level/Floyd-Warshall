S = input()
T = input()

def make(s, t):
    if s == t:
        print(1)
        exit()

    if len(s) > len(t):
        return

    if t[-1] == 'A':
        make(s, t[:-1])
    if t[0] == 'B':
        temp_t = t[::-1]
        make(s, temp_t[:-1])

make(S, T)

print(0)
