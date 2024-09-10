from collections import defaultdict

def solution(clothes):
    clothes_dict = defaultdict(int)
    for clothes_name, clothes_type in clothes:
        clothes_dict[clothes_type] += 1

    answer = 1
    for key, value in clothes_dict.items():
        answer = answer * (value + 1) # 아무것도 선택 안하는 경우 포함한 경우의 수
    return answer - 1 # 아무것도 안입는 경우 1개 빼기
