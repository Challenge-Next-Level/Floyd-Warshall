A, B, C, X, Y = map(int, input().split())

answer = 0


if X >= 1 and Y >= 1:
    basic_and_red_1_price = min(2 * C, A + B)
    basic_and_red_count = min(X, Y)
    answer += basic_and_red_count * basic_and_red_1_price
    X -= basic_and_red_count
    Y -= basic_and_red_count

if X > 0:
    answer += min(A, 2 * C) * X

if Y > 0:
    answer += min(B, 2 * C) * Y


print(answer)