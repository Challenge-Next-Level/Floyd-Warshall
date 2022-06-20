# 말 4개

# 0 -> 1, 1-> 2,3 로 이동 가능 [[1][2,3]]
graph = [[1], [2], [3], [4], [5], [6, 21],
         [7], [8], [9], [10], [11, 25],
         [11], [12], [13], [14], [15], [16, ],
         [17], [18], [19], [20], [32],
         [22], [23], [24],
         [30], [26], [24],
         [28], [29], [24],
         [31], [20], [32]]

score = [0, 2, 4, 6, 8, 10,
         12, 14, 16, 18, 20,
         22, 24, 26, 28, 30,
         32, 34, 36, 38, 40,
         13, 16, 19,
         25, 22, 24,
         28, 27, 26,
         30, 35, 0]

# 10개의 수 미리 입력
dice = list(map(int, input().split()))

def backtracking(count, result, horse): # 말들의 총 이동횟수, 더한 결과, 말들의 위치 list
    global answer
    if count >= 10:
        answer = max(answer, result)
        return

    for i in range(4):
        move = horse[i] # 현재말의 시작지점
        if len(graph[move]) == 2: # 첫칸은 분기가 될 수 있으니 조건을 걸고 이동
            move = graph[move][1]
        else:
            move = graph[move][0]

        for j in range(1, dice[count]): # 나머지칸 이동
            move = graph[move][0]

        if move == 32 or (move < 32 and move not in horse): # 말이 '도착'으로 이동, 도착이 아닌 곳으로 이동하면서 그곳에 말이 없을 때
            # 말을 이동하는 경우로 탐색
            before = horse[i]
            horse[i] = move
            backtracking(count + 1, result + score[move], horse)
            horse[i] = before


backtracking(0, 0, [0, 0, 0, 0])
print(answer)