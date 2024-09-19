def solution(sizes):
    bigger_side = list()
    smaller_side = list()

    for size in sizes:
        width, height = size[0], size[1]

        if width > height:
            bigger_side.append(width)
            smaller_side.append(height)
        else:
            bigger_side.append(height)
            smaller_side.append(width)
    answer = max(bigger_side) * max(smaller_side)
    return answer
