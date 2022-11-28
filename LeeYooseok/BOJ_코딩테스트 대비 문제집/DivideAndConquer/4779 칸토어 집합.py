def solution(start, end, n):
    global result
    if n == 0:
        return
    else:
        # 가운데 비움
        result = result[:start + 3 ** (n - 1)] + " " * (3 ** (n - 1)) + result[end - (3 ** (n - 1)) + 1:]
        # 왼쪽, 오른쪽 부분에 대해서 재귀 함수 수행
        solution(start, start + 3 ** (n - 1) - 1, n - 1)
        solution(end - (3 ** (n - 1)) + 1, end, n - 1)


while True:
    try:
        n = input()

        n = int(n)

        result = "-" * (3 ** n)

        solution(0, 3 ** n - 1, n)

        print(result)
    except EOFError:
        brea