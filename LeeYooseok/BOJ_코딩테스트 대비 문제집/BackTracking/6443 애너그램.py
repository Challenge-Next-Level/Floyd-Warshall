import sys


def back_tracking(cnt):

    # 현재 문자 길이가 입력된 문자 길이와 같다면 출력
    if cnt == len(word):
        print("".join(answer))
        return

    # 반복문을 통해 visited에 단어를 확인
    for k in visited:
        if visited[k]:
            visited[k] -= 1 # k를 사용할 것으로 -1
            answer.append(k) # answer에 더해준다.
            back_tracking(cnt + 1) # 백트래킹
            visited[k] += 1 # k를 사용안한 것으로 +1
            answer.pop() # answer에서 빼준다.


n = int(sys.stdin.readline())

for _ in range(n):
    word = sorted(list(map(str, sys.stdin.readline().strip())))
    visited = {}
    answer = []

    # 반복문을 통해 visited에 알파벳의 개수를 입력
    for i in word:
        if i in visited:
            visited[i] += 1
        else:
            visited[i] = 1

    # 백트래킹
    back_tracking(0)