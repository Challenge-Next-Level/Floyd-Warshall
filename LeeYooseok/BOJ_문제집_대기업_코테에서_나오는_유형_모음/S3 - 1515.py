import sys

input = sys.stdin.readline

number = input().rstrip()

answer = 0
idx = 0

while True:
    answer += 1

    for n in str(answer):
        if n == number[idx]:
            idx += 1
            if idx >= len(number):
                print(answer)
                exit()