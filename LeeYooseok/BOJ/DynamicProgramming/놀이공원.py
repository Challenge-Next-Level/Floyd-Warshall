import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
	N, K = map(int, input().split())
	board = [list(map(int, input().split())) for _ in range(N)]

	answer = 1e9

	for _y in range(N - K + 1):
		for _x in range(N - K + 1):
			now_value = 0
			for k in range(K):
				now_value += sum(board[_y + k][_x:_x + K])

			answer = min(answer, now_value)

	print(answer)
