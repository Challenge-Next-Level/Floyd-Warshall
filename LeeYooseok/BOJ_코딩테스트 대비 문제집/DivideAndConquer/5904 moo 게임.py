N = int(input())

i = 0
size = 3
# 몇번째 수열?
while size < N:
    i += 1
    size = size * 2 + (i + 3)


def solve(_size, midSize, idx):
    front = (_size - midSize) // 2
    if idx <= front:  # 앞 부분에 있다면
        return solve(front, midSize - 1, idx)
    elif idx > front + midSize:  # 뒷 부분에 있다면
        return solve(front, midSize - 1, idx - front - midSize)
    else:  # 중간에 있다면
        if idx - front == 1:  # 첫 번째 글자만 m이다, 나머진 o
            return 'm'
        else:
            return 'o'
