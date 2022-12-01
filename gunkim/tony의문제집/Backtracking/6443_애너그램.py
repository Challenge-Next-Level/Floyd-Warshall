import sys

n = int(input())
words = []
for _ in range(n):
    words.append(sys.stdin.readline().split()[0])


def dfs(ans, alphas, anagram, total_len):
    if len(anagram) >= total_len: # dfs 종료 조건
        ans.append(anagram)
        return
    for i in range(26):
        if alphas[i] <= 0:
            continue
        alphas[i] -= 1
        dfs(answer, alphas, anagram+chr(i+97), total_len)
        alphas[i] += 1


for i in range(n):
    answer = []
    length = len(words[i])
    # 초기 자료 생성
    alpha = [0] * 26
    for idx in range(length): # 알파벳 별로 갯수 저장
        alpha[ord(words[i][idx])-97] += 1
    # 탐색
    for j in range(26):
        if alpha[j] <= 0:
            continue
        alpha[j] -= 1
        dfs(answer, alpha, chr(j+97), length)
        alpha[j] += 1
    # 결과 출력
    answer.sort()
    for i in range(len(answer)):
        print(answer[i])