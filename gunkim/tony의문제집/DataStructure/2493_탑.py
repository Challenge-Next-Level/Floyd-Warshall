# 스택_큐 활용을 생각은 했는데 거꾸로 탐색하는 방법으로 해결하다 보니 실패했다
# 정답은 순방향 탐색을 활용하는 것이었다.
import sys

n = int(sys.stdin.readline().split()[0])
tower = list(map(int, sys.stdin.readline().split())) # 타워 높이 입력 받기

answer = [0 for _ in range(n)]
stack = [] # 수신을 받을 수 있는 타워를 갱신한다
for i in range(n):
    while stack: # 수신을 받는 타워 중
        if tower[i] > stack[-1][0]: # i번 째 타워가 수신할 수 있는 타워보다 크면
            stack.pop() # 이후 필요없는 수신타워가 되기 때문에 pop
        else: # i 번째 타워의 신호를 받을 수 있는 타워일때
            answer[i] = stack[-1][1] + 1 # answer에 위치 저장
            break
    stack.append([tower[i], i])

print(' '.join(map(str, answer)))