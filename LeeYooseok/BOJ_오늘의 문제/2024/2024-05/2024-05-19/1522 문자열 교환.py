# 교환 후 연속된 a 문자열의 길이는 입력된 문자열 속 a의 개수와 같다.
# 즉, a 의 개수와 동일한 길이로 연속된 문자열을 슬라이싱 하고, 슬라이싱한 문자열 내부에 있는 b 와 외부에 있는 a 와 교환하면 a가 연속되게 된다.
# 이때 교환 횟수는 슬라이싱한 문자열 내부에 있는 b 의 개수와 동일하다.

import sys

s = sys.stdin.readline().strip()

a_cnt = s.count("a")

s = s + s  # 문자열 시작과 끝이 연결되어 있음

answer = sys.maxsize
for i in range(len(s) - a_cnt):
    window = s[i:i + a_cnt]  # a 개수 -> 윈도우의 크기
    answer = min(answer, window.count("b"))  # 현재 윈도우에서 b의 개수 -> 움직여야 할 횟수

print(answer)
