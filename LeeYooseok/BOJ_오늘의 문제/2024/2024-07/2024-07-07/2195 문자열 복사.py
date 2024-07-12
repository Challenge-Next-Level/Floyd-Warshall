import sys

input = sys.stdin.readline

S = input().strip()
P = input().strip()

index_p = 0  # 현재 P에서 확인하고 있는 문자의 인덱스
ans = 0  # copy의 횟수

while index_p < len(P):
    # max_value : 현재 P와 S에서 확인하고 있는 가장 긴 부분 문자열의 길이
    # temp : 현재 확인 중인 길이
    # index_s : 현재 S에서 확인하고 있는 문자의 인덱스
    max_value, temp, index_s = 0, 0, 0

    while index_s < len(S) and index_p + temp < len(P):
        if P[index_p + temp] == S[index_s]:
            temp += 1
            max_value = max(max_value, temp)
        else:
            temp = 0
        index_s += 1
    index_p += max_value
    ans += 1

print(ans)
