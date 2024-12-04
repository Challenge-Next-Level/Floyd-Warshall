from decimal import Decimal, ROUND_HALF_UP

S = input()

P_H, P_G = 0, 0

for char in S:
    if char in {'H', 'P', 'Y'}:
        P_H += 1
    elif char in {'S', 'D'}:
        P_G += 1
    elif char == 'A':
        P_H += 1
        P_G += 1
answer = 50
if not(P_H == 0 and P_G == 0):
    answer = P_H / (P_H + P_G) * 100
rounded_value = Decimal(answer).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
print(f"{rounded_value:.2f}")
