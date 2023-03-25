N = int(input())
num_set = set(list(map(int, input().split())))

M = int(input())
num_list = list(map(int, input().split()))

for num in num_list:
    if num in num_set:
        print(1)
    else:
        print(0)