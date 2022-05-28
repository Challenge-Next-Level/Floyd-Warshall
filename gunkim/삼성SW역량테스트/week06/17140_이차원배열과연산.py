# 골드 4라고 하기에는 말도 안되게 어려운 문제라고 생각한다
# 1. 행, 열에 대해 생각해야 한다. -> zip 으로 해결
# 2. 숫자의 출현 빈도를 계산하고 저장해둬야 한다. -> Counter모듈에 most_common으로 해결
# 3. 숫자, 빈도에 대한 정렬 수행 -> sort의 lambda로 해결
# 4. (가장 어렵다고 생각)r, c는 리스트의 인덱스 외 값을 가리킬 수 있음(index error가 발생 가능)
# -> try, except으로 해결

import sys
from collections import Counter

r, c, k = map(int, sys.stdin.readline().split())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(3)]


def rc(): # 행 정렬
    length = len(A)
    max_len = 0 # 행 길이가 최대인 것을 구하기 위함
    for i in range(length):
        a = []
        for j in A[i]: # 0값을 제외한 행 리스트를 만든다(중요)
            if j != 0:
                a.append(j)
        a = Counter(a).most_common() # 행 리스트를 최빈값으로 이루어진 리스트로 바꾼다(진짜 중요)
        a.sort(key=lambda x: (x[1], x[0])) # (빈도수 -> 숫자) 순위로 정렬한다
        A[i] = [] # A의 행을 초기화
        for first, second in a: # 위에서 구한 최빈값 리스트를 순서대로 채운다
            A[i].append(first)
            A[i].append(second)
        row_len = len(A[i])
        if max_len < row_len:
            max_len = row_len
    for i in range(length):
        for k in range(max_len - len(A[i])):
            A[i].append(0)
        A[i] = A[i][:100] # 열 길이가 100을 넘지 않게 자른다
    return


time = 0
while True:
    try: # 인덱스 에러를 잡을 수 있음
        if A[r - 1][c - 1] == k:
            break
    except:
        pass
    if time >= 101:
        time = -1
        break
    if len(A) >= len(A[0]): # r 연산
        rc()
    else: # c 연산
        A = list(zip(*A)) # 행, 렬 대칭
        rc()
        A = list(zip(*A))
    time += 1

print(time)