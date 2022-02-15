# 간과하고 있던 사실: 문자열도 서로 대소 비교가 가능하다.
# 확실히 다시 인지하고 갈 것: 이분탐색은 선형탐색(완전탐색) 보다 확실히 성능이 좋다.
import sys

N, M = map(int, sys.stdin.readline().split())
S = []
test = []
for _ in range(N):
    S.append(sys.stdin.readline().split()[0])
for _ in range(M):
    test.append(sys.stdin.readline().split()[0])
S.sort() # 집합의 단어들을 정렬한다. 우린 test 문자열을 이곳 집합에서 이분 탐색을 통해 <접두사>가 있는 위치를 찾을 것이다.
answer = 0

for i in range(M): # test해야 할 문자열
    length = len(test[i])
    left, right = 0, N - 1
    while left <= right: # 이분 탐색을 통해 접두사가 있는 위치를 찾는다. 물론 없을 수도 있다.
        mid = (left + right) // 2
        if test[i] < S[mid]:
            right = mid - 1
        else:
            left = mid + 1
        if test[i] == S[mid][:length]: # 각각의 단계에서 접두사가 있는지 체크를 한다.
            answer += 1
            break

print(answer)