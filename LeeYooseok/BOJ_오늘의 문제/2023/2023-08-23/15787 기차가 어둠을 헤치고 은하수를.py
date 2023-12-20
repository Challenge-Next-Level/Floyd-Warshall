N, M = map(int, input().split())

train_board = [[0 for _ in range(20)] for _ in range(N)]

for _ in range(M):
    operations = list(map(int, input().split()))

    if operations[0] < 3:
        n, i, x = operations
        i -= 1
        x -= 1
    else:
        n, i = operations
        i -= 1

    # i, x => i번째 기차에 x번째 좌석에 사람을 태운다. 이미 사람이 있다면, 아무런 행동을 하지 않는다.
    if n == 1:
        train_board[i][x] = 1
    # i, x => i번째 기차에 x번째 좌석에 사람을 하차시킨다. 사람이 없다면, 아무런 행동을 하지 않는다.
    elif n == 2:
        train_board[i][x] = 0
    # i -> i번째 기차에 앉아있는 승객들이 모두 한칸씩 뒤로간다. k번째 앉은 사람은 k+1번째로 이동하여 앉는다. 만약 20번째 자리에 사람이 앉아있었다면 그 사람은 이 명령 후에 하차한다.
    elif n == 3:
        train_board[i].insert(0, 0)
        train_board[i].pop()
    # 4 i : i번째 기차에 앉아있는 승객들이 모두 한칸씩 앞으로간다. k번째 앉은 사람은 k-1 번째 자리로 이동하여 앉는다. 만약 1번째 자리에 사람이 앉아있었다면 그 사람은 이 명령 후에 하차한다.
    else:
        train_board[i].append(0)
        train_board[i].pop(0)


train_set = set()
for train in train_board:
    train_set.add(''.join(str(e) for e in train))

print(len(train_set))