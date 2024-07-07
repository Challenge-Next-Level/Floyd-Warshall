S = list(input())
T = list(input())

# T -> S 로 갈 수 있는지
# 1) 문자열의 뒤에 A를 추가한다. -> 문자열의 뒤에 A 가 있다면, 맨 뒤를 제거한다.
# 문자열을 뒤집고 뒤에 B를 추가한다. -> 문자열의 맨 앞에 B 가 있다면, 맨 앞을 제거하고 뒤집는다.

while T:
    if T[-1] == "A":
        T.pop()
    elif T[-1] == "B":
        T.pop()
        T.reverse()
    if S == T:
        print(1)
        exit()

print(0)
