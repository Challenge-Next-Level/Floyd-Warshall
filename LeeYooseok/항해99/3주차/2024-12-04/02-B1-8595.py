import sys

input = sys.stdin.readline

import re

N = int(input())
S = input().rstrip()

replaced_S = re.sub('[a-zA-Z]', ' ', S)

answer = 0
for num in replaced_S.split():
    answer += int(num)
print(answer)