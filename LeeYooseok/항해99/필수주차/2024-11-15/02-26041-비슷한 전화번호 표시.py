import sys

input = sys.stdin.readline

A_list = list(input().split())
B = input().rstrip()
B_length = len(B)

answer = 0
for a in A_list:
    if a[:B_length] == B and len(a) > B_length:
        answer += 1

print(answer)