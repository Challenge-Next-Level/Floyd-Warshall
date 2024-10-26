import sys

input = sys.stdin.readline

# 0은 뒤에서부터 제거
# 1은 앞에서부터 제거
S = list(map(int, list(input().rstrip())))
to_remove_one = sum(S) // 2
to_remove_zero = (len(S) - sum(S)) // 2

# 0 제거
for i in range(len(S) - 1, -1, -1):
    if to_remove_zero == 0:
        break
    if S[i] == 0:
        S[i] = ''
        to_remove_zero -= 1

# 1 제거
for i in range(len(S)):
    if to_remove_one == 0:
        break
    if S[i] == 1:
        S[i] = ''
        to_remove_one -= 1

answer = ''
for s in S:
    if s != '':
        answer += str(s)
print(answer)