N = int(input())
A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))

A_list.sort()
B_list.sort(reverse = True)

answer = 0
for i in range(N):
    answer += (A_list[i] * B_list[i])

print(answer)