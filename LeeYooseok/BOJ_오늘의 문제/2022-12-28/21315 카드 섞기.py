N = int(input())
card_list = list(map(int, input().split()))

def mix(k):
    global init_card
    # 1) 카드 더미 중 밑에서 2**K 개의 카드를 더미의 맨 위로 올린다.
    temp_card = init_card[N - 2 ** k:]
    init_card = temp_card + init_card[:N - 2 ** k]

    # i(2 ≤ i ≤ K + 1)번째 단계는 직전에 맨 위로 올린 카드 중 밑에서 2**(K - i + 1)개의 카드를 더미의 맨 위로 올린다.
    for i in range(2, k + 2):
        len_t = len(temp_card)
        init_card = temp_card[len_t - (2 ** (k - i + 1)):] + temp_card[:len_t - (2 ** (k - i + 1))] + init_card[len_t:]
        temp_card = temp_card[len_t - (2 ** (k - i + 1)):]

k1 = 1
while k1 ** 2 <= N:
    k2 = 1
    while k2 ** 2 <= N:

        # 초기 카드
        init_card = [i for i in range(1, N + 1)]

        # 2번의 k 섞기
        mix(k1)
        mix(k2)

        if init_card == card_list:
            print(k1, k2)
            exit()

        k2 += 1
    k1 += 1
