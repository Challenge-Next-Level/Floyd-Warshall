N = int(input())
price_list = list()
price_set = set()
for _ in range(N):
    price, delivery = map(int, input().split())
    price_set.add(price)
    price_list.append([price, delivery])

profit, answer = 0, 0

for price in price_set:
    # profit 계산
    now_profit = 0
    for p, d in price_list:
        if p >= price and (price - d) > 0:
            now_profit += (price - d)
    if now_profit > profit:
        answer = price
        profit = now_profit
    elif now_profit == profit:
        answer = min(answer, price)

print(answer)