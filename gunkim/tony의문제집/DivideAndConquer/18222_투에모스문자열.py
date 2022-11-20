# 나는 문자열을 아예 만든 후 n번째 문자를 찾기로 했다. 그러나 '시간초과'란 결과를 받았고
# 투에모스 문자열에 대한 개념이 원래 있었고 이를 찾기 쉽게 점화식으로 정리한 것을 보았으나 아직 이해가 가지 않는다.
# 보다가 느낀 점은 이진법으로 문자열을 만든 후 찾을 수 있지 않을까 생각을 했는데,,, 모르겠다.
n = int(input())


def recursive(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    if num%2:
        return 1-recursive(num//2)
    else:
        return recursive(num//2)


print(recursive(n-1))