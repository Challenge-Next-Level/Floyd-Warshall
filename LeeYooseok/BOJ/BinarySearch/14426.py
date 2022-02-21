"""
이분 탐색으로 어떻게 풀지?
"""

n, m = map(int, input().split())

strings = [input() for _ in range(n)]
check = [input() for _ in range(m)]

result = 0

for c in check:
    for s in strings:
        if s[:len(c)] == c:
            result += 1
            break

print(result)