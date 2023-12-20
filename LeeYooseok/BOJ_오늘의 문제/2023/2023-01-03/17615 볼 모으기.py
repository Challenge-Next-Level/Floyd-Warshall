N = int(input())
input_ball_list = list(input())
red, blue = 0, 0

ball_list = [[input_ball_list[0]]]
if input_ball_list[0] == 'R':
    red += 1
else:
    blue += 1

for ball in input_ball_list[1:]:
    if ball == 'R':
        red += 1
    else:
        blue += 1

    if ball_list[-1][0] == ball:
        ball_list[-1].append(ball)
    else:
        ball_list.append([ball])

print(ball_list)
answer = min(red, blue)

cnt = 0
# 가장 첫번째 원소의 색상을 옮기는 것이 효율적
if ball_list[0][0] == 'R':
    answer = min(answer, red - len(ball_list[0]))
else:
    answer = min(answer, blue - len(ball_list[0]))

# 가장 마지막 원소의 색상을 옮기는 것이 효율적
if ball_list[-1][0] == 'R':
    answer = min(answer, red - len(ball_list[-1]))
else:
    answer = min(answer, blue - len(ball_list[-1]))
# 빨, 파 중 더 적은 개수, 가장 좌측 원소의 색상 기준으로 좌측으로 몰아넣기, 가장 우측 원소의 색상 기준으로 우측으로 몰아넣기 중 최소값이 정답

print(answer)
