import sys

N = int(input())
answer = []
for i in range(N): # 자료를 사용하기 편하게 입력 받은 값을 받아서 정제한다
    number, s, b = list(map(int, sys.stdin.readline().split()))
    num = []
    num.append(number // 100)
    number %= 100
    num.append(number // 10)
    number %= 10
    num.append(number)
    answer.append([num, s, b])
count = 0 # 답의 가능성 갯수
for i in range(1, 10): # 9 * 9 * 9 의 모든 경우에 대해 답이 될 수 있는지 확인
    for j in range(1, 10):
        for k in range(1, 10):
            if i == j or i == k or j == k: # 서로 다른 수
                continue
            correct = 0 # 정답을 만족하는지 체크
            for ans in answer:
                strike, ball = 0, 0
                if ans[0][0] == i: # 첫 번째 수에 대한 검사
                    strike += 1
                elif ans[0][0] == j or ans[0][0] == k:
                    ball += 1
                if ans[0][1] == j: # 두 번째 수에 대한 검사
                    strike += 1
                elif ans[0][1] == i or ans[0][1] == k:
                    ball += 1
                if ans[0][2] == k: # 세 번째 수에 대한 검사
                    strike += 1
                elif ans[0][2] == i or ans[0][2] == j:
                    ball += 1
                if strike == ans[1] and ball == ans[2]:
                    correct += 1
            if correct == N: # 정답을 모두 만족하면 경우의 수 +1
                count += 1
print(count)