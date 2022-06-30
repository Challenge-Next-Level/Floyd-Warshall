# datetime 라이브러리를 활용하는 문제 같았음
import sys
from datetime import datetime

N, L, F = list(sys.stdin.readline().split())
# 대여기간을 분으로 변환하기
basic = L.split('/')
basicDay = int(basic[0])
basicHour, basicMinute = map(int, basic[1].split(':'))
basicTotal = basicDay * 1440 + basicHour * 60 + basicMinute

dict = {} # 대여자의 물품목록, 대여시간을 기록
answer = {} # 반납자의 벌금 기록

for _ in range(int(N)):
    date1, date2, part, name = list(sys.stdin.readline().split())
    now = datetime.strptime(date1 + ' ' + date2, '%Y-%m-%d %H:%M') # datetime 활용 핵심
    flag = 0 # 반납하는지 체크
    if name not in dict:
        dict[name] = []
    for i in range(len(dict[name])):
        p, d = dict[name][i]
        if p == part: # 대여한 물건이라면
            diff_date = now - d # 반납날짜 - 대여날짜
            total = diff_date.days * 1440 + diff_date.seconds // 60 # 차이를 분으로 변환
            if total > basicTotal: # 벌금 기록
                if name not in answer:
                    answer[name] = 0
                answer[name] += (total-basicTotal) * int(F)
            del dict[name][i]
            flag = 1
            break
    if flag == 0: # 반납하는게 아니면 대여목록 추가
        dict[name].append([part, now])

if len(answer) == 0:
    print(-1)
else:
    answer = list(answer.items()) # dictionary를 list로 변환
    answer.sort()
    for i in range(len(answer)):
        print(answer[i][0], str(answer[i][1]))