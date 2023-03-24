N = int(input())
answer = [['B'] * N for _ in range(7)]


def make(start, end, layer):
    if layer == 7:
        return

    mid = (start + end) // 2
    for idx in range(start, mid + 1):
        answer[layer][idx] = 'A'

    make(start, mid, layer + 1)
    make(mid + 1, end, layer + 1)


make(0, N - 1, 0)

for a in answer:
    for _a in a[:-1]:
        print(_a, end="")
    print('B')
