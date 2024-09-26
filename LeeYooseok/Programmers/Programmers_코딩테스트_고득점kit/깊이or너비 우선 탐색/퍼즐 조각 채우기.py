from collections import deque


def solution(game_board, table):
    def find_blocks(board, target):
        block_list = list()

        m, n = len(board[0]), len(board)
        visited = [[False for _ in range(m)] for _ in range(n)]

        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        for _y in range(n):
            for _x in range(m):
                if board[_y][_x] == target and not visited[_y][_x]:
                    queue = deque()
                    queue.append([_x, _y])
                    visited[_y][_x] = True
                    block = [[_x, _y]]

                    while queue:
                        now_x, now_y = queue.popleft()

                        for i in range(4):
                            new_x, new_y = now_x + dx[i], now_y + dy[i]

                            if not (0 <= new_x < m) or not (0 <= new_y < n):
                                continue

                            if board[new_y][new_x] != target:
                                continue

                            if visited[new_y][new_x]:
                                continue

                            queue.append([new_x, new_y])
                            visited[new_y][new_x] = True
                            block.append([new_x, new_y])

                    block_list.append(block)

        return block_list

    def block_to_board(block):
        # 가로 크기, 세로 크기 확인 및 보드 만들기
        width, height = 0, 0
        # 시작 지점
        start_x, start_y = 1e9, 1e9
        for piece_x, piece_y in block:
            width, height, start_x, start_y = max(width, piece_x), max(height, piece_y), min(start_x, piece_x), min(
                start_y, piece_y)

        board = [[0 for _ in range(width - start_x + 1)] for _ in range(height - start_y + 1)]
        for piece_x, piece_y in block:
            board[piece_y - start_y][piece_x - start_x] = 1

        return board

    def rotate_board(board):
        rotated_board = [[0 for _ in range(len(board))] for _ in range(len(board[0]))]
        puzzle_size = 0

        for _y in range(len(board)):
            for _x in range(len(board[0])):
                if board[_y][_x] == 1:
                    puzzle_size += 1
                rotated_board[_x][len(board) - _y - 1] = board[_y][_x]

        return rotated_board, puzzle_size

    answer = 0

    empty_block_list = find_blocks(game_board, 0)
    puzzle_list = find_blocks(table, 1)

    for empty_block in empty_block_list:
        filled = False
        empty_board = block_to_board(empty_block)

        for puzzle in puzzle_list:
            if filled:
                break

            puzzle_board = block_to_board(puzzle)
            for _ in range(4):
                puzzle_board, puzzle_size = rotate_board(puzzle_board)

                if empty_board == puzzle_board:
                    answer += puzzle_size
                    puzzle_list.remove(puzzle)
                    filled = True
                    break

    return answer


game_board = [
    [1, 1, 0, 0, 1, 0],
    [0, 0, 1, 0, 1, 0],
    [0, 1, 1, 0, 0, 1],
    [1, 1, 0, 1, 1, 1],
    [1, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0, 0]
]

table = [
    [1, 0, 0, 1, 1, 0],
    [1, 0, 1, 0, 1, 0],
    [0, 1, 1, 0, 1, 1],
    [0, 0, 1, 0, 0, 0],
    [1, 1, 0, 1, 1, 0],
    [0, 1, 0, 0, 0, 0]
]

print(solution(game_board, table))
