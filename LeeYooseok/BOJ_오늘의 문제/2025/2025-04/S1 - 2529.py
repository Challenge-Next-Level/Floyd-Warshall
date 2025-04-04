k = int(input())
operation_list = input().split()

min_answer, max_answer = "", ""
visited = [False for _ in range(10)]


def check(a, b, operator):
    if operator == ">":
        return a > b
    else:
        return a < b


def solve(length, answer):
    global min_answer, max_answer
    if length == k + 1:
        if min_answer == "":
            min_answer = answer
        else:
            max_answer = answer
        return

    for i in range(10):
        if not visited[i]:
            if length == 0 or check(answer[-1], str(i), operation_list[length - 1]):
                visited[i] = True
                solve(length + 1, answer + str(i))
                visited[i] = False


solve(0, "")
print(max_answer)
print(min_answer)
