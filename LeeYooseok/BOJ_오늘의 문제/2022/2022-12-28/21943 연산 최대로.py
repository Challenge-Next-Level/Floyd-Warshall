N = int(input())
num_list = list(map(int, input().split()))
P, Q = map(int, input().split())
ans = 0


def solve(idx, num_set):
    global ans
    if idx == N:
        temp_ans = 1
        for nums in num_set:
            temp_ans *= sum(nums)
        ans = max(ans, temp_ans)
    else:
        for i in range(Q + 1):
            temp_list = [item[:] for item in num_set]
            temp_list[i].append(num_list[idx])
            solve(idx + 1, temp_list)
            temp_list[i].remove(num_list[idx])


if P != 0 and Q == 0:
    ans = sum(num_list)
elif P == 0 and Q != 0:
    ans = 1
    for num in num_list:
        ans *= num
else:
    # Q + 1 개의 묶음을 갖는 모든 조합을 만든다.
    # 인덱스를 활용해서 조합을 만듦.

    temp_answer = [[] for _ in range(Q + 1)]
    solve(0, temp_answer)

print(ans)
