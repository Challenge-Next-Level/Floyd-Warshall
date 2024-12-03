import sys

input = sys.stdin.readline

N = int(input())

answer = 0
building_list = [list(map(int, input().split())) for _ in range(N)]
building_list.append([0, 0])

stack = [0]

for building in building_list:
    y = building[1]

    # 이전 건물보다 높으면 stack 에 현재 건물 추가
    if stack[-1] < y:
        stack.append(y)
    # 이전 건물보다 낮아지면 이전의 건물들 중 현재 높이보다 낮은 건물을 다 빼준다.
    elif stack[-1] > y:
        # 이전의 건물이 여러개일 수 있다.
        now_height = y
        # 현재 건물의 높이보다 이전 건물들이 다 낮을 때 까지 stack에서 꺼내어 개수를 세준다.
        while stack[-1] > y:
            # 건물의 높이가 달라야지, 다른 건물임
            if stack[-1] != now_height:
                answer += 1
            now_height = stack.pop()
        # 현재 건물 stack에 넣어줌
        stack.append(y)

print(answer)
