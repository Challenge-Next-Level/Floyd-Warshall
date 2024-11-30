import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    school_list = list()
    for _ in range(N):
        S, L = input().split()
        school_list.append([int(L), S])

    school_list.sort(reverse = True)
    print(school_list[0][1])