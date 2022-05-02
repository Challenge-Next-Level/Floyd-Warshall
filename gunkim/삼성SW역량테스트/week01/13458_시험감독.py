import sys

n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
B, C = map(int, sys.stdin.readline().split())

answer = 0
for num in A:
    if num - B > 0:
        answer += (num - B) // C
        if (num - B) % C != 0:
            answer += 1
    answer += 1
print(answer)
