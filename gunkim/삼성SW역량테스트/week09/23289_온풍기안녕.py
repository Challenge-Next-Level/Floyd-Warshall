import sys

r, c, k = map(int, sys.stdin.readline().split())
board = []
for _ in range(r):
    board.append(list(map(int, sys.stdin.readline().split())))
w = int(sys.stdin.readline().split()[0])
wall = []
for _ in range(w):
    wall.append(list(map(int, sys.stdin.readline().split())))



# 모든 온풍기에서 바람이 한 번 나옴

# 2. 온도가 조절됨

# 3. 가장 바깥 쪽 칸의 온도는 1씩 감소

# 4. 초콜릿 먹기

# 5. 모든 칸의 온도가 k 이상이면 중단 or 1부터 다시 시작