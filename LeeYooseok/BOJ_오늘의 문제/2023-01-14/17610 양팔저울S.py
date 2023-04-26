# DFS 풀이

K = int(input())
gram_list = list(map(int, input().split()))
S = sum(gram_list)
possible_list = [1 for _ in range(S + 1)]


def use(now_value, now_idx):
    if now_idx == K:
        if 0 < now_value <= S:
            possible_list[now_value] = 0
    # elif now_value > S:
    #     return
    else:
        use(now_value + gram_list[now_idx], now_idx + 1)
        use(now_value - gram_list[now_idx], now_idx + 1)
        use(now_value, now_idx + 1)


# 만들 수 있는 경우의 수 체크
use(0, 0)

print(sum(possible_list) - 1)
