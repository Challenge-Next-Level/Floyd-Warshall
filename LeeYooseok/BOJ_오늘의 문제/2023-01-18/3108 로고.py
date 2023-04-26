N = int(input())

rectangle_dict = dict()

x1, y1, x2, y2 = map(int, input().split())
rectangle_dict[0] = [x1, x2, y1, y2, 1]


def chk_zero_move(rectangle):
    x1, x2, y1, y2 = rectangle[0], rectangle[1], rectangle[2], rectangle[3]
    if x1 == 0 or x2 == 0 or y1 == 0 or y2 == 0:
        return False
    else:
        return True


zero_move = chk_zero_move(rectangle_dict[0])


def check(now, target):
    if not now[0] < target[0] < now[1] and not now[0] < target[1] < now[1] and not now[2] < target[2] < now[3] and not now[2] < target[3] < now[3]:
        return False
    else:
        return True


group = 1
for i in range(1, N):
    x1, y1, x2, y2 = map(int, input().split())
    rectangle_now = [x1, x2, y1, y2]
    chk = True
    for rectangle in rectangle_dict.values():
        if check(rectangle_now, rectangle):
            rectangle_dict[i] = [x1, x2, y1, y2, rectangle[-1]]
            chk = False
            break

    if chk:
        group += 1
        rectangle_dict[i] = [x1, x2, y1, y2, group]

    if zero_move:
        zero_move = chk_zero_move(rectangle_now)

if zero_move:
    group += 1
print(group - 1)
