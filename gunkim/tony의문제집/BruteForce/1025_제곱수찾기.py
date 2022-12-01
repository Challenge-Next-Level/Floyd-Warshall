# 과감하게 4중 for문을 사용해야 한다는 것도 중요하고
# 무엇보다 행, 열에 대한 공차를 2중 for문으로 만드는 것도 내가 접근하기 어려웠던 생각이다.
# 다만 하나 의문이 있다면 공차의 시작의 -n+1, -m+1이 더 맞는 것 같은데 틀린 정답이라고 한다.
import sys
import math

n, m = map(int, input().split())
words = []
for _ in range(n):
    words.append(sys.stdin.readline()[:-1])
answer = -1

# (0,0) ~ (n-1,m-1) 모든 지점에서 시작 가능
for i in range(n):
    for j in range(m):
        for y in range(-n,n): # y축 공차
            for x in range(-m, m): # x축 공차
                if y == 0 and x == 0:
                    continue
                ny, nx = i, j
                string = ''
                while 0<=ny<n and 0<=nx<m:
                    string += words[ny][nx]
                    number = int(string)
                    numberSqrt = math.sqrt(number)
                    if numberSqrt - int(numberSqrt) == 0:
                        answer = max(answer, number)
                    ny += y
                    nx += x
print(answer)