# 백트래킹 보다는 브루트 포스에 더 가까운 문제 같다,,,
n = int(input())

result = []
number = ''
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def dfs(): # 모든 경우의 숫자를 만든다
    global number
    if len(number) > 0: # 결과에 추가
        result.append(int(number))

    for i in range(10):
        if len(number) == 0 or numbers[i] > number[0]:
            number = numbers[i] + number
            dfs()
            number = number[1:]


dfs()
result.sort()
if len(result) < n:
    print(-1)
else:
    print(result[n-1])