"""
3, 3*3, 3*3*3,
1 : 1
2 : 2
3 : 4
4 : 11
5 : 12
6 : 14
10 : 41
11 : 42
12 : 44
"""


def solution(n):
    q = n // 3
    r = n % 3

    if r == 0:
        q -= 1 # 0이 필요 없기 때문에, 나머지가 0으로 떨어지는 경우가 있으면 몫을 하나 낮추어서 나머지가 3이 되도록
        answer = '4'
    else:
        answer = str(r)

    if n <= 3:
        return answer
    else:
        return solution(q) + answer


print(solution(513))

