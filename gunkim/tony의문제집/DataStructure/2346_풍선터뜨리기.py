import sys

n = int(sys.stdin.readline().split()[0])
case = list(map(int, sys.stdin.readline().split()))
balloon = []
for idx in range(n):
    balloon.append([case[idx], idx + 1]) # 풍선이 가진 숫자, 풍선의 번호

i = 0 # 완전 인덱스로만 생각
answer = []
while len(balloon) > 1:
    move = balloon[i][0] # 움직여야 할 칸
    answer.append(balloon[i][1])
    del balloon[i] # 풍선 터뜨리기
    length = len(balloon) # 터뜨리고 난 뒤 남은 풍선 수

    if i == length: # 리스트 맨 마지막 풍선이 터졌을 때
        i = length - 1 # 인덱스 수정을 해줘야 함
        if move < 0:
            move += 1
    else:
        if move > 0:
            move -= 1
    move %= length
    i = (i + move + length) % length
answer.append(balloon[0][1]) # 마지막 풍선 추가
print(' '.join(map(str, answer)))