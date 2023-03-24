num_list = list()
while True:
    try:
        num_list.append(int(input()))
    except:
        break

max_num = max(num_list)
answer = ['-'] * (3 ** max_num)


def solve(start, end, size):
    for idx in range(start + size, end - size):
        answer[idx] = ' '

    if size > 1:
        next_size = size // 3
        solve(start, start + size, next_size)
        solve(end - size, end, next_size)


solve(0, 3 ** max_num, 3 ** (max_num - 1))

for num in num_list:
    for a in answer[:(3 ** num)]:
        print(a, end="")
    print()
