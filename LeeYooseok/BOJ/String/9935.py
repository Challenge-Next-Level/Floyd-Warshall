"""
replace 가 시간복잡도 : 원본 string 의 길이만큼 소요됨

    1. 입력문자열을 앞에서부터 차례차례 한 글자씩 스택에 push 합니다.
    2. 현재 글자가 폭발 문자열의 마지막 글자와 일치하면 스택의 top부터 폭발문자열의 길이까지 확인하여 폭발문자열이 만들어지는지 확인합니다.
    3. 폭발문자열이 만들어진다면 만들어지는 폭발문자열을 스택에서 pop합니다.
    4. 1~3을 반복합니다.
    5. 문자열 순회를 마치고 스택이 비어있으면, FRULA를 출력, 비어있지 않다면 스택_큐 속 문자열을 차례로 출력합니다.
"""

text = input()
bomb = input()

last_bomb = bomb[-1]
length_bomb = len(bomb)

temp = []
for t in text:
    temp.append(t)

    if t == last_bomb and ''.join(temp[-length_bomb:]) == bomb:
        del temp[-length_bomb:]

answer = ''.join(temp)

if answer == '':
    print("FRULA")
else:
    print(answer)