import sys

input = sys.stdin.readline

S = input().rstrip()

a_count = S.count("a")

S = S + S  # 문자열 시작과 끝이 연결되어 있음

answer = sys.maxsize

for i in range(len(S) - a_count):
    window = S[i:i + a_count]
    answer = min(answer, window.count("b"))

print(answer)
