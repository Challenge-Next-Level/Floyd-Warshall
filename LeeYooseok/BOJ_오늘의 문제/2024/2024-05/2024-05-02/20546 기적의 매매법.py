import sys

input = sys.stdin.readline

cash = int(input())
stock_price_list = list(map(int, input().split()))

# 준현 주가 계산
JH_stock = 0
JH_cash = cash

# 성민 주가 계산
SM_stock = 0
SM_cash = cash
increase_cnt = 0
decrease_cnt = 0

for i in range(14):
    now_stock_price = stock_price_list[i]

    if JH_cash >= now_stock_price:
        JH_stock += (JH_cash // now_stock_price)
        JH_cash = JH_cash % now_stock_price

    if i > 0:
        prior_stock_price = stock_price_list[i - 1]

        if (now_stock_price - prior_stock_price) > 0:
            increase_cnt += 1
            decrease_cnt = 0

        if (now_stock_price - prior_stock_price) < 0:
            increase_cnt = 0
            decrease_cnt += 1

    if increase_cnt >= 3:
        SM_cash += SM_stock * now_stock_price
        SM_stock = 0

    if decrease_cnt >= 3:
        SM_stock += (SM_cash // now_stock_price)
        SM_cash = (SM_cash % now_stock_price)

JH_cash += JH_stock * stock_price_list[-1]
SM_cash += SM_stock * stock_price_list[-1]

if JH_cash > SM_cash:
    print("BNP")
elif JH_cash < SM_cash:
    print("TIMING")
else:
    print("SAMESAME")

