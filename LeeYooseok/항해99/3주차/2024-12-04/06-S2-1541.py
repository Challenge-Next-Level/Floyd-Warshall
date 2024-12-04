import sys

input = sys.stdin.readline

S = input().rstrip()

split_S = S.split("-")

answer = 0
for num in split_S[0].split("+"):
    answer += int(num)

for s in split_S[1:]:
    temp_num = 0
    for num in s.split("+"):
        temp_num += int(num)
    answer -= temp_num


print(answer)