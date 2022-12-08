import sys

input = sys.stdin.readline

N = int(input())

hwakjangja_dict = dict()

for _ in range(N):
    file_name_list = input().strip().split(".")
    hwakjangja = file_name_list[1]


    if hwakjangja in hwakjangja_dict.keys():
        hwakjangja_dict[hwakjangja] += 1
    else:
        hwakjangja_dict[hwakjangja] = 1


for item in sorted(hwakjangja_dict.items()):
    print(item[0], item[1])