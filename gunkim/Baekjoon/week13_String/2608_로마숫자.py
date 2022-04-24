alpha_lst = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
value_lst = [1, 5, 10, 50, 100, 500, 1000]

# 딕셔너리로 만든 것 같음
alhpa_to_value = {i:j for i,j in zip(alpha_lst, value_lst)}
value_to_alpha = {i:j for i,j in zip(value_lst, alpha_lst)}

a = input()
b = input()


value = 0
for v in [a, b]: # 로마 문자를 숫자로 치환하여 더해주는 과정
    value += alhpa_to_value[v[-1]]
    for i in range(len(v)-1):
        if alhpa_to_value[v[i]] < alhpa_to_value[v[i+1]]:
            value -= alhpa_to_value[v[i]]
        else:
            value += alhpa_to_value[v[i]]
print(value) # 모두 더한 값 출력


# 핵심은 4, 9 단 2개의 예외 처리만 한다는 점, 연속으로 문자를 사용한다 뭐 이런 것들 처리 필요x
for v in value_lst[::-1]: # 숫자를 로마 문자로 치환하는 과정
    while value >= v:
        if str(value)[0] == "4": # 4의 경우 예외 처리
            value -= 4*v
            print(value_to_alpha[v], end="")
            print(value_to_alpha[v*5], end="")
        elif str(value)[0] == "9": # 9의 경우 예외 처리
            v //= 5
            value -= 9*v
            print(value_to_alpha[v], end="")
            print(value_to_alpha[v*10], end="")
        else:
            value -= v
            print(value_to_alpha[v], end="")