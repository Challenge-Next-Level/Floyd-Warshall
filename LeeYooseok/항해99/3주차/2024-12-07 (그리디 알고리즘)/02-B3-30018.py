import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

answer = sum([abs(A[i] - B[i]) for i in range(N)]) // 2

print(answer)