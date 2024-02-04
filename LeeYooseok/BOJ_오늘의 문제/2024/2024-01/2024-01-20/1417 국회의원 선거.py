N = int(input())

dasom = int(input())
vote_list = [int(input()) for _ in range(N - 1)]
vote_list.sort(reverse=True)

if N == 1:
    print(0)
else:
    answer = 0
    # 표가 제일 많은 후보를 찍으려고 하는사람을 매수
    while vote_list[0] >= dasom:
        dasom += 1
        vote_list[0] -= 1
        answer += 1
        vote_list.sort(reverse=True)
    print(answer)