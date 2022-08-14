import sys

n = int(input())
liquid_list = list(map(int, input().split()))

liquid_list.sort()

# 2 pointer 설정
s_p = 0
e_p = n-1

check = sys.maxsize
answer = list()

while s_p < e_p:
    liquid_1 = liquid_list[s_p]
    liquid_2 = liquid_list[e_p]

    if abs(liquid_1 + liquid_2) < check:
        check = abs(liquid_1 + liquid_2)
        answer = [liquid_1, liquid_2]

    # 두 용액의합이 0보다 작다면 왼쪽의 값을 늘려 조금 더 0에 가깝게 만들어준다
    if liquid_1 + liquid_2 < 0:
        s_p += 1
    # 반대로, 두 용액의 합이 0보다 크다면 오른쪽의 값을 줄여서 조금 더 0에 가깝게 만들어준다
    else:
        e_p -= 1

print(answer[0], answer[1])
