# 1부터 N까지의 수로 이루어진 순열

num_text = input()
visited = [False for _ in range(len(num_text))]
num_len = len(num_text)

def dfs(index, arr):
    if index == num_len:
        print(*arr)
        exit()

    # 1자리수 check
    num1 = int(num_text[index])
    if not visited[num1]:
        visited[num1] = True
        arr.append(num1)
        dfs(index + 1, arr)
        visited[num1] = False
        arr.pop()

    # 2자리수 check
    if index+1 < num_len:
        num2 = int(num_text[index:index+2])
        if num2 <= N and not visited[num2]:
            visited[num2] = True
            arr.append(num2)
            dfs(index+2, arr)
            visited[num2] = False
            arr.pop()

# N이 무엇인지 알아낸다.
if num_len < 10:
    N = num_len
else:
    N = ((num_len - 9) // 2) + 9

dfs(0, [])


