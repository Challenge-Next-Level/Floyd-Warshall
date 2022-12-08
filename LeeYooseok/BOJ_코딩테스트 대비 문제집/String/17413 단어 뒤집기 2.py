# 문자열의 시작과 끝은 공백이 아니다.
from collections import deque

import sys

input = sys.stdin.readline

S = input().strip()

text_deque = deque()

status = 'close'

for s in S:
    if s == '<' and status == 'close':
        while text_deque:
            print(text_deque.pop(), end="")
        print("<", end="")
        status = 'open'
    elif s == '>' and status == 'open':
        while text_deque:
            print(text_deque.popleft(), end="")
        print(">", end="")
        status = 'close'
    elif s == ' ' and status == 'close':
        while text_deque:
            print(text_deque.pop(), end="")
        print(' ', end="")
    else:
        text_deque.append(s)


while text_deque:
    print(text_deque.pop(), end="")


