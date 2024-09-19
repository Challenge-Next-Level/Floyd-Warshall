def solution(brown, yellow):
    # brown + 4 = (가로 + 세로) * 2
    # yellow = (가로 - 2) * (세로 - 2)

    sum_width_height = (brown + 4) // 2
    for i in range(1, sum_width_height // 2 + 1):
        height = i
        width = sum_width_height - height

        if yellow == (width - 2) * (height - 2):
            return [width, height]

print(solution(8, 1))