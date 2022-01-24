# 내가 이 풀이 전에 시도했던 방법: 재귀 -> 모든 경로를 따져가며 탐색, 당연히 시간초과...
N = int(input())
# 사자 배치 경우의 수(XX, OX, XO) 총 3가지
case = [[-1] * 3 for _ in range(N + 1)]
for i in range(3): # N = 1일때 초기값 세팅
    case[1][i] = 1
# 0은 XX, 1은 XO, 2는 OX로 배치하는 경우
# 예를 들어, XO로 배치하는 경우 이전에 XX, OX로 배치한 경우에만 배치할 수 있다
for i in range(2, N + 1):
    case[i][0] = (case[i - 1][0] + case[i - 1][1] + case[i - 1][2]) % 9901
    case[i][1] = (case[i - 1][0] + case[i - 1][2]) % 9901
    case[i][2] = (case[i - 1][0] + case[i - 1][1]) % 9901

print((case[N][0] + case[N][1] + case[N][2]) % 9901)