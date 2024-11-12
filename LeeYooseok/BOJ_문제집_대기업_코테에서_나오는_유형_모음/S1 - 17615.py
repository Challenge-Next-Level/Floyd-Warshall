# 양 끝에있는 볼을 기준으로 옮긴다.

N = int(input())
ball_list = list(input())

red, blue = 0, 0
for ball in ball_list:
    if ball == "R":
        red += 1
    else:
        blue += 1

# 가운데 있는 공을 옮기는 경우
answer = min(red, blue)

# 왼쪽 볼 기준
left_cnt = 0
left_ball = ball_list[0]
consequence = True
for ball in ball_list[1:]:
    if ball == left_ball and consequence:
        continue
    elif ball != left_ball:
        consequence = False
    elif ball == left_ball and not consequence:
        left_cnt += 1

# 오른쪽 볼 기준
right_cnt = 0
right_ball = ball_list[-1]
consequence = True
for ball_idx in range(N - 2, -1, -1):
    ball = ball_list[ball_idx]
    if ball == right_ball and consequence:
        continue
    elif ball != right_ball:
        consequence = False
    elif ball == right_ball and not consequence:
        right_cnt += 1

print(min(answer, left_cnt, right_cnt))
