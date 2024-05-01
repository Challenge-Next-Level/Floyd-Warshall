import sys

input = sys.stdin.readline

class Node:
    def __init__(self):
        self.end = False  # 단어의 마지막 노드인지 표시
        self.children = {}  # 노드의 자식 dictionary

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, food_list):
        node = self.root

        for food in food_list:
            if food not in node.children:
                node.children[food] = Node() # 자식 노드
            node = node.children[food]
        node.end = True

    def search(self, depth, now_node):
        if now_node.end:
            return

        now_children = sorted(now_node.children.keys())

        for child in now_children:
            print("--" * depth + child)
            self.search(depth + 1, now_node.children[child])


trie = Trie()
N = int(input())
for _ in range(N):
    eat_info = list(input().split())
    K = eat_info.pop(0)
    trie.insert(eat_info)

trie.search(0, trie.root)

