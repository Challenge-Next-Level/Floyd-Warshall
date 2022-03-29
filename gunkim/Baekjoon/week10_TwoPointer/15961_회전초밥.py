# 우선 python3로 제출시 '시간초과'가 발생하니 pypy3로 제출해야 한다
import sys
from collections import defaultdict

# 유의점: k <= N이란 조건이 있으므로 주인공은
# 1번 행사에 무조건 참여가 가능. 즉 서비스 초밥을 무조건 먹을 수 있음
# 이것을 모르고 따로 예외 처리를 해야 하는 줄 알았다
N, d, k, c = map(int, sys.stdin.readline().split())
sushi = []
for _ in range(N):
    sushi.append(int(sys.stdin.readline()))
sushi.extend(sushi)

answer = 0
left, right = 0, 0
eat_sushi = defaultdict(int) # 이 문제를 해결하기 위해 쓰기 좋은 자료형
eat_sushi[c] += 1 # 쿠폰으로 먹는 경우 미리 추가

for right in range(len(sushi)):
    eat_sushi[sushi[right]] += 1 # 초밥을 먹는다
    if right + 1 >= k: # k개를 먹었다면 정답 갱신 및 left값 +1
        answer = max(answer, len(eat_sushi))
        eat_sushi[sushi[left]] -= 1
        if eat_sushi[sushi[left]] == 0:
            del eat_sushi[sushi[left]]
        left += 1
print(answer)