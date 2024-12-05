L = int(input())
X = input()

M = 1234567891
r = 31

answer = 0

for i in range(L):
    num = ord(X[i]) - 96
    answer += (num * (r ** i))

print(answer % M)