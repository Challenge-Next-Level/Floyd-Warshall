import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())

    rank_list = [list(map(int, input().split())) for _ in range(N)]
    rank_list.sort()

    highest_interview_rank = rank_list[0][1]
    # 첫번째 사람은 무조건 채용
    answer = 1
    for i in range(1, N):
        # i번째 사람의 면접 순위가 i-1번째 사람들의 면접 순위보다 더 높으면
        if rank_list[i][1] < highest_interview_rank:
            highest_interview_rank = rank_list[i][1]
            answer += 1

    print(answer)

