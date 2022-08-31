n = int(input())
calender = [0] * 366

for _ in range(n):
    s, e = map(int, input().split(' '))

    for i in range(s, e + 1):
        # 해당 날짜에 몇개의 일정이 있는지 카운트
        calender[i] += 1

row = 0
col = 0
ans = 0
for i in range(366):
    if calender[i] != 0:
        row = max(row, calender[i])
        col += 1
    else:
        # 일정 면적 계산
        ans += row * col
        row = 0
        col = 0
ans += row * col
print(ans)