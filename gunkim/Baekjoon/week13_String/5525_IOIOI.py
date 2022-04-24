# 처음에 Pn을 직접 만들어 사용을 해서 인지 test2를 통과하지 못했다.
import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
s = sys.stdin.readline()

answer = count = i = 0
while i < m - 1:
    if s[i:i + 3] == 'IOI': # IOI일 때 카운트 증가
        count += 1
        i += 2
        if count == n: # 카운트가 n이 라면 answer 증가
            answer += 1
            count -= 1
    else: # 아니면 바로 초기화
        count = 0
        i += 1
print(answer)