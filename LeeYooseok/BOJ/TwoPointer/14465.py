"""
슬라이딩 윈도우
투포인터와 유사하게 start, end 두개의 포인터로 푼다. -> 정렬 안해도 상관없고, 사이 요소들의 개수 세는 것
"""

import sys

input = sys.stdin.readline

N, K, B = map(int, input().split())
data = [1] * (N + 1)  # 정상 신호등 = 1

for i in range(B):
    data[int(input())] = 0  # 고장 신호등 = 0

broken = 0
min_value = K  # 고친 신호등 개수 초기화 : K (최대 개수 - 연속적으로 K개 정상이어야 함)

for left in range(1, N + 1):
    if left > (N - K + 1):  # 데이터 검색 끝 : 연속적으로 K개 정상이어야 하기 때문에, left가 N-K 부터 시작하면 신호등 개수가 K개가 안됨
        break
    else:
        right = left + K - 1  # right 값 갱신 - K 개의 신호등 검사

        for item in data[left:right + 1]:
            if item == 0:  # 해당 신호등 고쳐야 한다면,
                broken += 1
            if broken >= min_value:  # 최솟값보다 크게 나오면 바로 반복문 탈출
                break
        min_value = min(min_value, broken)
        broken = 0  # 초기화시켜줌

print(min_value)
