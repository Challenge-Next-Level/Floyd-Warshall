# 질문 검색에 있던 어떤 사람의 질문으로 문제 해결책을 이해함
import sys

test = int(input())
for _ in range(test):
    paper = list(sys.stdin.readline()[:-1])
    flag = 0

    def divideAndConquer(start, size):
        global flag
        if flag == 1 or size == 1:
            return
        # 1. 종이를 중앙을 기준으로 양쪽 종이로 나눔
        # 2. 양쪽 종이는 서로 꺽인 방향이 반대임
        # 3. 예를 들어 종이가 ABCDEFG 로 표현되어 있다면 D는 중앙이 되고 ABC, EFG 종이를 비교해야 함.
        # A의 반대는 G가 되고, C의 반대가 E가 되는 것임
        for i in range(size//2):
            if paper[start+i] == paper[start+size-1-i]:
                flag = 1
                return
        divideAndConquer(start, size//2)
        divideAndConquer(start+(size//2)+1, size//2)
        return


    divideAndConquer(0, len(paper))
    if flag == 0:
        print('YES')
    else:
        print('NO')