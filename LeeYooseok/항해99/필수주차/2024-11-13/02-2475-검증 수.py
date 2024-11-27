import sys

input = sys.stdin.readline

number_list = list(map(int, input().split()))
answer = 0
for number in number_list:
    answer += (number ** 2)

print(answer % 10)