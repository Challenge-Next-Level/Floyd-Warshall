# 정규 표현식을 이용한 문제
# ^ 해당 패턴으로 시작
# ? 해당 패턴을 0번또는 1번
# + 해당 패턴이 하나 이상
# $ 해당 패턴으로 끝

import re
p = re.compile('^[A-F]?A+F+C+[A-F]?$')
for _ in range(int(input())):
    print('Good' if p.match(input()) is None else 'Infected!')