# r[i]와 r[j]이 각각 M으로 나눴을 때의 나머지가 동일하다면 빼기 연산 후 나머지는 0이 돼 M으로 나눠떨어지게 된다.

import sys

input = sys.stdin.readline
n, m = map(int, input().split())  # n : 숫자 갯수, m : 나눌 수 
num = list(map(int, input().split())) + [0]  # 숫자 입력
r = [0] * m  # 누적합을 m으로 나눴을 때의 나머지가 index 인 누적합 개수

for i in range(n):
    num[i] += num[i - 1]  # 숫자 정보를 누적합으로 갱신
    r[num[i] % m] += 1  # 해당 누적합을 m으로 나눴을 때의 나머지에 해당하는 값에 1추가

cnt = r[0]  # 구간이 없을 때 : i == j 일때

for i in r:  # 나머지가 동일한 구간들 중 서로 다른 2개 선택 -> 부분합 빼면 나머지 : 0
    cnt += i * (i - 1) // 2

print(cnt)
