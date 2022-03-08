import sys

N, M = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))


def divideSection(value): # 투포인터 알고리즘 활용이다. 2개의 포인터 max,min 을 통해 구간의 최대차이를 만든다. 이를 value 와 비교한다.
    # 첫 번째 구간 설정
    max_val = min_val = num[0]
    cnt = 1
    # 구간 크기를 늘려가며 value 보다 크지 않게 구간을 만든다
    for i in range(1, N):
        max_val = max(max_val, num[i])
        min_val = min(min_val, num[i])
        if max_val - min_val > value: # num[i]를 구간에 포함시키면서 value 를 넘기 때문에 새로운 구간을 만들어 num[i] 부터 구간을 시작한다.
            print(num[i])
            cnt += 1
            max_val = num[i]
            min_val = num[i]
    return cnt


start, end = 0, max(num)
answer = 0
while start <= end:  # 구간의 차이의 최댓값을 직접 설정을 하며 이분탐색을 한다.
    mid = (start + end) // 2
    if divideSection(mid) <= M:  # 구간의 갯수가 M을 만족하거나 적을 때 값을 작게 만들어 구간이 더 많이 나오게 한다.
        end = mid - 1
        answer = mid
    else:
        start = mid + 1

print(answer)