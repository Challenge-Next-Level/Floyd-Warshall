T = int(input())

for _ in range(T):
    a, b = map(int, input().split())

    a_set = set()
    b_set = set()

    while a != 1:
        a_set.add(a)
        a = a // 2

    while b != 1:
        b_set.add(b)
        b = b // 2

    common_parent = a_set.intersection(b_set)
    common_parent.add(1)
    print(10 * max(common_parent))