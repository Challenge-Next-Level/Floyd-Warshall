from collections import defaultdict, deque

w = int(input())
word_dict = defaultdict(list)
for _ in range(w):
    word = input()
    len_word = len(word)
    score = 0
    if len_word < 3:
        score = 0
    elif 3 <= len_word <= 4:
        score = 1
    elif len_word == 5:
        score = 2
    elif len_word == 6:
        score = 3
    elif len_word == 7:
        score = 5
    elif len_word == 8:
        score = 11
    word_dict[word[0]].append([word, score])

input()

dx = [1, 1, 0, -1, -1, -1, 0, 1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

b = int(input())


def dfs(depth, w, s, now_y, now_x):
    global total_score, word_set, max_word
    if w in word_set:
        return
    if depth + 1 == len(w):
        total_score += s
        word_set.add(w)

        if len(max_word) == len(word):
            max_word = min(max_word, word)
        elif len(word) > len(max_word):
            max_word = word

        return

    for i in range(8):
        new_y, new_x = now_y + dy[i], now_x + dx[i]

        if not (0 <= new_y < 4) or not (0 <= new_x < 4):
            continue

        if visited[new_y][new_x] == 1:
            continue

        if board[new_y][new_x] != w[depth + 1]:
            continue

        visited[new_y][new_x] = 1
        dfs(depth + 1, w, s, new_y, new_x)
        visited[new_y][new_x] = 0


for b_idx in range(b):
    board = [list(input()) for _ in range(4)]

    if b_idx < b - 1:
        input()

    total_score = 0
    max_word = ''
    word_set = set()

    visited = [[0 for _ in range(4)] for _ in range(4)]

    for _y in range(4):
        for _x in range(4):
            if board[_y][_x] in word_dict.keys():

                visited[_y][_x] = 1

                for word, score in word_dict[board[_y][_x]]:
                    dfs(0, word, score, _y, _x)

                visited[_y][_x] = 0

    print(total_score, max_word, len(word_set))
