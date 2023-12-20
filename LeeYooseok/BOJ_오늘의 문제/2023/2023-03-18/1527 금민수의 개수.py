A, B = map(int, input().split())
answer = 0

def solve(num):
    global answer
    if num <= B:
        if A <= num:
            answer += 1
        solve(num * 10 + 4)
        solve(num * 10 + 7)
    else:
        return

solve(4)
solve(7)

print(answer)
