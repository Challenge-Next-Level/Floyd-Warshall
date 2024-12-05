N = int(input())

dasom = int(input())
vote_list = [int(input()) for _ in range(N - 1)]

# 후보자가 다솜 혼자
if N == 1:
    print(0)
else:
    answer = 0
    while dasom <= max(vote_list):
        vote_list[vote_list.index(max(vote_list))] -= 1
        dasom += 1
        answer += 1
    print(answer)