import sys
read = sys.stdin.readline

word1, word2 = read().strip(), read().strip()
l1, l2 = len(word1), len(word2)
# matrix 표 생성, 이때 초기값을 따로 더 만들어야 해서 +1로 칸을 늘린다
matrix = [[0] * (l2 + 1) for _ in range(l1 + 1)]

for i in range(1, l1 + 1): # 1번째 줄 부터 matrix표를 채워간다. (word1의 i번째 까지 문자열)
    for j in range(1, l2 + 1): # word2의 j번째 까지 문자열과 비교
        if word1[i - 1] == word2[j - 1]: # 비교하는 문자가 같다면 [i - 1][j - 1] + 1
            matrix[i][j] = matrix[i - 1][j - 1] + 1
        else: # 아니라면 max([i - 1][j], [i][j - 1])
            matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1])
print(matrix[l1][l2])