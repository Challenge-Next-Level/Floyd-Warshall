import sys

T = int(input())
for _ in range(T):
    N = int(input())
    log = list(map(int, sys.stdin.readline().split()))
    log.sort(reverse=True) # 큰 통나무부터 사용하기 위해 정렬
    answer = 0
    left, right = log[0], log[0] # 제일 큰 통나무 기준으로 양쪽에 통나무들을 놓을 것이다
    for i in range(1, N): # 통나무들을 왼쪽, 오른쪽 번갈아 가며 놓는다, 그때 높이의 차이를 구한다
        if i % 2 == 0:
            answer = max(answer, left - log[i])
            left = log[i]
        else:
            answer = max(answer, right - log[i])
            right = log[i]
    print(answer)