"""
sys.stdin.readline 으로 하면 문자열 입력 길이가 1일때 2가 나와서 틀린다. -> 개행문자도 같이 입력을 받기 때문에 잘라줘야 한다.
"""

n = int(input())

talk = input()
length = len(talk)

start = 0
end = 1

result = 0

if length == 1:
    print(1)
elif len(set(talk)) <= n:
    print(len(talk))
else:
    while end < length:
        temp = len(set(talk[start:end + 1]))
        cnt = end-start+1
        if cnt < result:
            end += 1
            continue

        if temp == n:
            result = max(result, cnt)
            end += 1
            continue

        if temp < n:
            end += 1
            continue

        if temp > n:
            start += 1
            continue

    print(result)
