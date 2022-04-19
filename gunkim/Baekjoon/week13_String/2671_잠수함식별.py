import re


S = str(input())
p = re.compile('(100+1+|01)+')
m = p.fullmatch(S)

if m:
    print('SUBMARINE')
else:
    print('NOISE')