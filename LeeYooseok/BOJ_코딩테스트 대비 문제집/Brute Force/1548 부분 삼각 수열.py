# arr[0] + arr[1] > arr[n-1]을 만족한다면 n-1 과 a 사이에 있는 모든 수들이 삼각관계이다.
# 주어진 수열의 길이가 2 이하인 경우, 항상 삼각 수열이라고 친다.
# 이는, 주어진 수열의 길이가 3이상인 경우 결과값의 최솟값은 2임을 의미하기도 한다.

N = int(input())
num_list = [map(int, input().split())]

num_list.sort() # 정렬된 상태에서,

# num_list 길이가 3 보다 작으면 해당 수가 답이된다.
answer = N

if N > 2:
    answer = -1
    for start in range(N - 2):
        for end in range(N - 1, start + 1, -1):
            if num_list[start] + num_list[start + 1] > num_list[end]:
                answer = max(answer, end - start + 1)

    if answer == -1:
        answer = 2
print(answer)
