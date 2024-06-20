# https://ip99202.github.io/posts/%EB%B0%B1%EC%A4%80-10252-%EA%B7%B8%EB%A6%AC%EB%94%94-%EA%B7%B8%EB%9E%98%ED%94%84/

T = int(input())
for _ in range(T):
    m, n = map(int, input().split())
    print(1)
    for _y in range(m):
        if _y == 0:
            print(f'({_y}, {0})')
        if _y % 2 == 0:
            for _x in range(1, n):
                print(f'({_y}, {_x})')
        else:
            for _x in range(n - 1, 0, -1):
                print(f'({_y}, {_x})')

    for _y in range(m - 1, 0, -1):
        print(f'({_y}, {0})')

