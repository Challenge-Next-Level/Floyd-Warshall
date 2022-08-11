import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coin_list = list()
answer = sys.maxsize
for _ in range(n):
    coin_list.append(int(input()))

def check(cnt, price):
    global answer
    chk = False
    for c in coin_list:
        temp_price = price + c

        if temp_price == k:
            chk = True
            answer = min(answer, cnt + 1)
        elif temp_price > k:
            continue
        else:
            if cnt < answer:
                chk = True
                check(cnt + 1, temp_price)
    if not chk:
        return


for coin in coin_list:
    check(1, coin)

if answer == sys.maxsize:
    print(-1)
else:
    print(answer)
