# https://velog.io/@rhdmstj17/%EB%B0%B1%EC%A4%80-1052%EB%B2%88-%EB%AC%BC%EB%B3%91-python-%EB%B9%84%ED%8A%B8%EB%A7%88%EC%8A%A4%ED%82%B9

n, k = map(int, input().split())
answer = 0
while bin(n).count('1') > k:
    idx = bin(n)[::-1].index('1') # 1이 오른쪽에서 몇 번째에 있는지 찾기
    answer += 2 ** idx # 2 ^ (idx) 만큼 더하기
    n += 2 ** idx # 2 ^ (idx) 만큼 더하기
print(answer)