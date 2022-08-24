# 딕셔너리로 저장하는 것은 시간초과 발생, 이것도 완전탐색이다.
# 투 포인터를 활용하여 시간복잡도를 줄인다.
# python3 로 채점하면 시간초과 발생.
import sys

n = int(input())
A, B, C, D = [0 for _ in range(n)], [0 for _ in range(n)], [0 for _ in range(n)], [0 for _ in range(n)]

for i in range(n):
    A[i], B[i], C[i], D[i] = map(int, sys.stdin.readline().split())

AB, CD = [], []
for i in range(n):
    for j in range(n):
        AB.append(A[i] + B[j])
        CD.append(C[i] + D[j])
AB.sort()
CD.sort()

# AB에 left 인덱스를 놓고, CD에 right 인덱스를 놓는다.
left, right = 0, len(CD) - 1
answer = 0
while left < len(AB) and right >= 0:
    if AB[left] + CD[right] == 0: # 합이 0일 때
        nextL, nextR = left + 1, right - 1 # 같은 값을 찾아
        while nextL < len(AB) and AB[left] == AB[nextL]:
            nextL += 1
        while nextR >= 0 and CD[right] == CD[nextR]:
            nextR -= 1
        answer += (nextL - left) * (right - nextR) # 갯수만큼 결과 값에 더한다.
        left, right = nextL, nextR
    elif AB[left] + CD[right] > 0: # 합이 0보다 클 때
        right -= 1
    else: # 합이 0보다 작을 때
        left += 1
print(answer)