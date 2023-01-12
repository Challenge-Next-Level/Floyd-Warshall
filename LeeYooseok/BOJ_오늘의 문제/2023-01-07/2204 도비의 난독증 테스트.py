import sys

input = sys.stdin.readline
answer = list()
while True:
    n = int(input())
    if n == 0:
        break

    word_list = [[input().strip(), i] for i in range(n)]
    temp_list = [item[:] for item in word_list]

    for w in word_list:
        w[0] = w[0].lower()

    word_list.sort(key=lambda x: x[0])

    answer.append(temp_list[word_list[0][1]][0])

for a in answer:
    print(a)
