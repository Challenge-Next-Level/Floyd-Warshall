# 앞 쪽(stack)과만 비교하면 되는데 뒤 까지 비교해서 븅신같이 틀렸던 문제
n, k = map(int, input().split())
problem = str(input())


stack = []
count = 0
for i in range(n):
    while count < k and stack and stack[-1] < problem[i]:
        stack.pop()
        count += 1
    stack.append(problem[i])


print(''.join(stack[:n-k]))