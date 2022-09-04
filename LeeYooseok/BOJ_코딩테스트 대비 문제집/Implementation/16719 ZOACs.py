import sys
input = sys.stdin.readline

S = list(input().rstrip())
result = ['']*len(S)


def func(arr, start):
    if not arr:
        return
    _min = min(arr) # 제일 사전순 앞의 알파벳을 찾음
    idx = arr.index(_min) # 위치(start + idx)를 찾음
    result[start+idx] = _min # 해당 위치에 해당 단어를 넣어줌

    print("".join(result))

    func(arr[idx+1:], start+idx+1) # 현재 단어의 오른쪽을 먼저 확인
    func(arr[:idx], start) # 현재 단어의 왼쪽을 이후에 확인


func(S, 0)