# 정규 표현식(Regular Expressions)에 대해 공부
# 복잡한 문자열을 처리할 때 사용하는 기법, 어느 정도 고급 주제이다.
import re


S = str(input())
p = re.compile('(100+1+|01)+')
m = p.fullmatch(S)

if m:
    print('SUBMARINE')
else:
    print('NOISE')