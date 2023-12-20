K = int(input())
gram_list = list(map(int, input().split()))
S = sum(gram_list)
possible_list = [1 for _ in range(S + 1)]


def use(use_list, now_value, start_idx):
    if 0 < now_value <= S:
        possible_list[now_value] = 0

    for i in range(start_idx, K):
        if not use_list[i]:
            use_list[i] = True
            use(use_list, now_value + gram_list[i], i + 1)
            use(use_list, now_value - gram_list[i], i + 1)
            use_list[i] = False


# 만들 수 있는 경우의 수 체크
use_check = [False for _ in range(K)]
for i in range(K):
    use_check[i] = True
    use(use_check, gram_list[i], i + 1)
    use(use_check, -1 * gram_list[i], i + 1)
    use_check[i] = False

print(sum(possible_list) - 1)