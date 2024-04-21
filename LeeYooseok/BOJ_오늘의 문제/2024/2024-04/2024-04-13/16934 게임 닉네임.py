# 별칭 : 유저 닉네임의 접두사 중에서 가장 길이가 짧은 것
# 동일한 접두사 사용 X
# 가능한 별칭이 없는 경우 - 유저 닉네임 X(동일한 닉네임으로 가입한 유저 수)
import sys
from collections import defaultdict

input = sys.stdin.readline

class Node:
    def __init__(self):
        self.end = False  # 단어의 마지막 노드인지 표시
        self.children = {}  # 노드의 자식 dictionary


class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word):
        node = self.root

        for char in word:  # char = word 의 한 글자
            if char not in node.children:  # char 가 노드 의 children 에 없다면, 노드 추가
                node.children[char] = Node()
            node = node.children[char]  # 다음 노드로 변경
        alias_dict[word] += 1
        node.end = True  # 단어의 마지막 노드 표시

    def search(self, word):
        node = self.root
        alias = ''
        for char in word:
            alias += char
            if char not in node.children:  # 자식 dictionary 에 char 없다면 -> nickname 반환
                return alias
            node = node.children[char]

        # 가능한 별칭이 없는 경우
        if node.end:
            alias += str(alias_dict[alias] + 1)
        return alias


N = int(input())
tree = Trie()
alias_dict = defaultdict(int)
for _ in range(N):
    nickname = input().rstrip()
    print(tree.search(nickname))
    tree.insert(nickname)
