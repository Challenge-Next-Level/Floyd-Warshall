# 한 자리씩 늘리며 사전순으로 가장 빠른 문자열 만들기
# 뒤 문자열 부터 만들며 앞 문자열을 붙이는 느낌(?)은 파악했는데 재귀로 이를 구현해야겠다고는 생각지도 못함
word = input()

length = len(word)
answer = ['' for _ in range(length)]


def makeRightAndLeft(arr, startIdx):
    if not arr:
        return
    minWord = 'a'
    idx = -1
    for i in range(len(arr)): # arr에서 가장 작은 알파벳 찾기
        if arr[i] < minWord:
            minWord = arr[i]
            idx = i
    answer[startIdx+idx] = minWord
    print(''.join(answer)) # 출력하기
    makeRightAndLeft(arr[idx+1:], startIdx+idx+1) # 뒷 문자열(Right) 먼저 찾기
    makeRightAndLeft(arr[:idx], startIdx) # 앞 문자열(Left) 찾기
    return


makeRightAndLeft(list(word), 0)