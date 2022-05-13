import sys

n = int(sys.stdin.readline())
board = []
total = 0
for i in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))
    total += sum(board[i])
answer = float('inf')
size = n // 2


def team_away(nums, idx, depth, res):
    if idx == size:
        print("jojo", res)
        return int(res)
    cal = 0
    for i in range(idx + 1, size):
        cal += board[nums[idx]][nums[i]] + board[nums[i]][nums[idx]]
        print("cal", cal)
    team_away(nums, idx + 1, depth + 1, res + cal)
    return


def team(nums, depth, result):
    global answer
    if depth == size:
        nums_away, j = [], 0
        for i in range(n):
            if j < size and nums[j] == i:
                j += 1
                continue
            nums_away.append(i)
        print(nums_away)
        x = int(team_away(nums_away, 0, 1, 0))
        print(x)
        answer = min(answer, abs(result - x))
        return
    if n - nums[-1] <= size - depth:
        return
    for idx in range(nums[-1] + 1, n):
        cal = 0
        for num in nums:
            cal += board[num][idx] + board[idx][num]
        nums.append(idx)
        team(nums, depth + 1, result + cal)
        nums.pop()


for i in range(size + 1):
    team([i], 1, 0)

print(answer)