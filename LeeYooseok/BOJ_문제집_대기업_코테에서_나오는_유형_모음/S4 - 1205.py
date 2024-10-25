N, new_score, P = map(int, input().split())
if N == 0:
    print(1)
else:
    ranking_list = list(map(int, input().split()))
    if N == P and new_score <= ranking_list[-1]:
        print(-1)
    else:
        answer = N + 1
        for i in range(N):
            if ranking_list[i] <= new_score:
                answer = i + 1
                break
        print(answer)
