N = int(input())

pattern = input().split("*")
length = len(pattern[0]) + len(pattern[1])

for _ in range(N):
    file = input()
    if length > len(file):
        print("NE") # 표현 불가능

    else:
        if pattern[0] == file[:len(pattern[0])] and pattern[1] == file[-len(pattern[1]):]:
            print("DA") # 표현 가능
        else:
            print("NE")
