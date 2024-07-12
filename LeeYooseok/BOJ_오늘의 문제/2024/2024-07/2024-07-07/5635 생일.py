import sys

input = sys.stdin.readline

n = int(input())

people_list = list()
for _ in range(n):
    name, day, month, year = input().split()

    people_list.append([int(year), int(month), int(day), name])

people_list.sort()

print(people_list[-1][-1])
print(people_list[0][-1])