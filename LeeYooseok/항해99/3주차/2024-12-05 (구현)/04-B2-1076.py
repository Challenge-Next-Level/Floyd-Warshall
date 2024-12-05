import sys

input = sys.stdin.readline

table = {
    "black": [0, 1],
    "brown": [1, 10],
    "red": [2, 100],
    "orange": [3, 1_000],
    "yellow": [4, 10_000],
    "green": [5, 100_000],
    "blue": [6, 1_000_000],
    "violet": [7, 10_000_000],
    "grey": [8, 100_000_000],
    "white": [9, 1_000_000_000]
}

answer = 0
answer += (10 * table[input().rstrip()][0])
answer += table[input().rstrip()][0]
answer *= table[input().rstrip()][1]

print(answer)
