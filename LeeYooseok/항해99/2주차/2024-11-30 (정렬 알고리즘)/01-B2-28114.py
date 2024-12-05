import sys

input = sys.stdin.readline

first_method = list()
second_method = list()


for _ in range(3):
    P, Y, S = input().split()

    first_method.append(int(Y) % 100)
    second_method.append([int(P), S[0]])

first_method.sort()
second_method.sort(reverse=True)

print("".join(list(map(str, first_method))))
print("".join([item[1] for item in second_method]))