import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    char_list = list(input().split())

    answer = char_list[0]
    for char in char_list[1:]:
        if char <= answer[0]:
            answer = char + answer
        else:
            answer = answer + char
    print(answer)