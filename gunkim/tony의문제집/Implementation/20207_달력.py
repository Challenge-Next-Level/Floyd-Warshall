import sys

n = int(input())
schedule = []
for _ in range(n):
    schedule.append(list(map(int, sys.stdin.readline().split())))

# 날짜마다 일정이 몇개 있는지 카운트
date = [0 for _ in range(367)]
for i in range(n):
    start, end = schedule[i]
    for j in range(start, end+1):
        date[j] += 1

day = 1 # 현재 날짜
flag = 0 # 연속된 일정을 세고 있는지 확인하는 플래그
start = -1 # 연속된 일정의 첫 시작
answer = 0
while day <= 366:
    if date[day] > 0:
        if flag == 0:
            start = day
            flag = 1
    else:
        if flag == 1:
            answer += max(date[start:day]) * (day-start)
            start = -1
            flag = 0
    day += 1
print(answer)