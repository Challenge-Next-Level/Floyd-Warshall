x, y, c = map(float, input().split())

left = 0
right = min(x, y)
res = 0


def find_c(x, y, w):
    hx = (x ** 2 - w ** 2) ** 0.5
    hy = (y ** 2 - w ** 2) ** 0.5
    # w1 : c = w : h2, w2 : c = w : h1
    # w1 = c*w / h2, w2 = c*w / h1
    # w = w1 + w2 = c*w / h2 + c*w / h1 = c*w*(h1+h2) / (h1*h2)
    # 1 = c*(h1+h2) / (h1*h2)
    c = (hx * hy) / (hx + hy)
    return c


while right - left > 0.000001:
    mid = (left + right) / 2

    if find_c(x, y, mid) >= c:
        res = mid
        left = mid
    else:
        right = mid

print(res)