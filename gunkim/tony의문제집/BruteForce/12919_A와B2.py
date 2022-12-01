# S -> T로 만드는 과정으로 dfs 구현을 했다. 이때 visit 메모리를 추가로 사용했는데 '메모리 초과'가 발생
# 다른 분의 의견을 통해 T -> S로 만드는 과정으로 구현을 하면 visit 메모리는 필요하지 않게됨.
# 그리고 모든 경우의 수를 보지 않아도 됨. 
S = input()
T = input()
answer = 0
L = len(S)


def dfs(string):
    if len(string) < L:
        return
    if len(string) == L and string == S:
        global answer
        answer = 1
        return
    # 두 가지의 연산
    if string[-1] == 'A':
        dfs(string[:-1])
    if string[0] == 'B':
        dfs(string[:0:-1])
    return


dfs(T)
print(answer)