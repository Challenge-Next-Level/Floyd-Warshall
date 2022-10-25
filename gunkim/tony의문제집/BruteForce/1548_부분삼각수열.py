# 우선 리스트를 정렬하기!
# 오름차순의 a,b,c는 a+b>c 만족시 삼각관계도 자동으로 만족한다.
import sys

n = int(sys.stdin.readline().split()[0])
A = list(map(int, sys.stdin.readline().split()))
length = len(A)
answer = 0
A.sort()


for first in range(0, length-2):
    for third in range(length-1,first+1,-1):
        second = first+1
        if A[first]+A[second] > A[third]:
            answer = max(answer, third-first+1)
            break

if answer != 0:
    print(answer)
elif length == 1:
    print(1)
else:
    print(2)