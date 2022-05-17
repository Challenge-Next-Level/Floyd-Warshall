import sys

gear = [0] * 4
for i in range(4): # 톱니바퀴 입력 받기
    gear[i] = sys.stdin.readline()[:-1]

case = []
k = int(sys.stdin.readline())
for _ in range(k): # 회전시키는 케이스 입력 받기
    case.append(list(map(int, sys.stdin.readline().split())))

teeth = [[6,2], [6,2], [6,2], [6,2]] # 각 톱니 좌우의 index (중요!)
for g, d in case:
    g -= 1
    info = [0] * 4 # 각 톱니가 어느 방향으로 회전하는지 저장
    info[g] = -d # index값 계산을 쉽게 하기 위해 ex.시계방향 회전시(+1) index를 -1해야함
    # 좌측 비교
    for left in range(g, 0, -1):
        if gear[left][teeth[left][0]] == gear[left - 1][teeth[left - 1][1]]:
            break
        info[left - 1] = info[left] * -1
    # 우측 비교
    for right in range(g, 3):
        if gear[right][teeth[right][1]] == gear[right + 1][teeth[right + 1][0]]:
            break
        info[right + 1] = info[right] * -1
    # 회전 하는 방향 정보를 가지고 index 값 계산
    for i in range(4):
        teeth[i][0] = (teeth[i][0] + info[i]) % 8
        teeth[i][1] = (teeth[i][1] + info[i]) % 8

result = 0
for i in range(4): # 결과 값 계산
    if gear[i][teeth[i][1] - 2] == '1':
        if i == 0:
            result += 1
        elif i == 1:
            result += 2
        elif i == 2:
            result += 4
        elif i == 3:
            result += 8
print(result)


