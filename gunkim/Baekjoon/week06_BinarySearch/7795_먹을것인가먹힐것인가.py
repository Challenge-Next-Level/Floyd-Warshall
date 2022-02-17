import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    A = list(map(int, sys.stdin.readline().split()))
    B = list(map(int, sys.stdin.readline().split()))
    B.sort() # 이분탐색을 위해 정렬 필수
    answer = 0 # A가 B보다 큰 쌍의 갯수(총합)

    for i in range(len(A)): # 모든 A에 대해 이분 탐색
        left, right = 0, len(B) - 1
        cnt = 0 # A가 B보다 큰 쌍의 갯수
        while left <= right:
            mid = (left + right) // 2 # 중간 index를 설정
            if A[i] <= B[mid]:
                right = mid - 1
            else:
                left = mid + 1
                cnt = left
        answer += cnt

    print(answer)