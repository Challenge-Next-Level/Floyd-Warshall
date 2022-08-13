import sys
from collections import defaultdict

n, d, k, c = map(int, sys.stdin.readline().split())
sushi = []
for _ in range(n):
    sushi.append(int(sys.stdin.readline()))

if n != k: # 회전 초밥이기 때문에 뒤에 리스트를 더 추가
    sushi += sushi[:k-1]

eat = defaultdict(int) # 먹는 초밥의 종류를 dict로 저장
eat[c] += 1 # 쿠폰으로 먹기 추가
left, right = 0, 0
answer = 0
for right in range(len(sushi)): # 브루트포스
    eat[sushi[right]] += 1
    if right + 1 >= k:
        answer = max(answer, len(eat))
        eat[sushi[left]] -= 1 # left에 있는 초밥 제거
        if eat[sushi[left]] == 0: # 0개가 되면 dict에서 아예 delete
            del eat[sushi[left]]
        left += 1
print(answer)