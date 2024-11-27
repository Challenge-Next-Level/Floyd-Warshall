n = int(input())

recursion = 0


def fibo(_n):
    global recursion

    if _n == 1 or _n == 2:
        # 함수 호출 횟수 확인
        recursion += 1
        return 1
    else:
        return fibo(_n - 1) + fibo(_n - 2)


fibo(n)

print(recursion, n - 2)