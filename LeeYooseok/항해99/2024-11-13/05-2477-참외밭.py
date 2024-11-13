import sys

input = sys.stdin.readline

# (참외의 개수 / 1 단위 면적)
K = int(input())

# 전체 가로 및 세로 길이
width, height = 0, 0
width_idx, height_idx = 0, 0
# 변 리스트
side_list = list()
for i in range(6):
    d, size = map(int, input().split())
    # d 가 가로면
    if d == 1 or d == 2:
        if size > width:
            width = size
            width_idx = i
    else:
        if size > height:
            height = size
            height_idx = i
    side_list.append(size)

# 가로 및 세로 양옆에 붙어있는 변을 확인하기 위해 양 끝에 추가
side_list.insert(0, side_list[-1])
side_list.append(side_list[1])
# index 1 증가
width_idx += 1
height_idx += 1


# 작은 사각형 가로 및 세로 길이
part_width, part_height = 0, 0
# 작은 사각형 가로 길이 = 전체 사각형 가로 - (전체 사각형 세로에 붙어있는 작은 가로)
part_width = width - min(side_list[height_idx - 1], side_list[height_idx + 1])
# 작은 사각형 세로 길이 = 전체 사각형 세로 - (전체 사각형 가로에 붙어있는 작은 세로)
part_height = height - min(side_list[width_idx - 1], side_list[width_idx + 1])

# 정답 : (전체 사각형 넓이 - 작은 사각형 넓이) * (참외의 개수 / 1 단위 면적)
answer = (width * height - part_width * part_height) * K
print(answer)
