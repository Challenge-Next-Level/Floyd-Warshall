import sys

text = list(input())
n = int(input())
cursor = len(text)

for i in range(n):
    command = sys.stdin.readline().split()

    if command[0] == "L" and cursor > 0:
        cursor -= 1
    elif command[0] == "D" and cursor < len(text):
        cursor += 1
    elif command[0] == "B" and cursor > 0:
        text.pop(cursor-1)
        cursor -= 1
    elif command[0] == "P":
        text.insert(cursor, command[1])
        cursor += 1

for i in range(len(text)):
    print(text[i], end="")