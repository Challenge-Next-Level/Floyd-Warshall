# 주어진 재료는 딱 한 번씩 밖에 사용 못함. (처음에 여러번 사용해도 되는줄 알았음)
import sys

n = int(input())
things = []
for _ in range(n):
    things.append(list(map(int, sys.stdin.readline().split())))

answer = float('inf')


# index를 전달해서 이전에 탐색했던 재료는 굳이 탐색하지 않도록 함. '시간초과' 발생을 막을 수 있었음.
def dfs(visi, sour, bitter, index):
    global answer
    if abs(sour-bitter) < answer:
        answer = abs(sour-bitter)
    for i in range(index+1, n):
        if visi[i]:
            continue
        s, b = things[i]
        visi[i] = True
        dfs(visi, sour*s, bitter+b, i)
        visi[i] = False


for i in range(n):
    visit = [False for _ in range(n)]
    visit[i] = True
    dfs(visit, things[i][0], things[i][1], i)

print(answer)