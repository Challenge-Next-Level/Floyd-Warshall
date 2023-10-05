class Node(object):
    def __init__(self, key, mark=0, data=None):
        self.key = key
        self.mark = mark
        self.data = data
        self.children = {} # dict

class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        cur = self.head

        for char in string: # 각 캐릭터 순회
            # 해당 캐릭터가 트리에 없을경우 하위 노드로 추가
            if char not in cur.children.keys():
                cur.children[char] = Node(char)
            cur = cur.children[char] # 현재 노드 변경

        # 마지막 노드의 경우 data를 스트링으로 변경하여 마지막 노드임을 명시
        cur.data = string

    def marking(self, string):
        # insert 과정과 유사하나 삭제하지 말아야 하는 부분(char)에 mark 를 1로 설정한다.
        cur = self.head

        for char in string:
            cur.mark = 1
            if char not in cur.children.keys():
                cur.children[char] = Node(char)
            cur = cur.children[char]
        cur.mark = 1

    def remove(self, string):
        cur = self.head

        result = 0
        for char in string:
            # 해당 캐릭터가 있고 해당 캐릭터가 mark가 되어있으면 계속 순회
            if char in cur.children.keys() and cur.children[char].mark == 1:
                cur = cur.children[char]
            # 이미 삭제한 부분이면 종료해도 된다. 상위 명력어로 전부 삭제 가능하기 때문이다.
            elif cur.children[char].mark == 2:
                return result
            # 삭제 가능한 경우 mark를 2로 바꿔주고 return 해준다.
            else:
                result += 1
                cur.children[char].mark = 2
                return result

        # 해당 단어 전체를 삭제 명령어로 써야하는 경우
        result += 1
        return result

T = int(input())

for _ in range(T):
    trie = Trie()

    remove_file_name_list = list()
    N_1 = int(input())
    for _ in range(N_1):
        file_name = input()
        remove_file_name_list.append(file_name)
        trie.insert(file_name)

    N_2 = int(input())
    for _ in range(N_2):
        file_name = input()
        trie.marking(file_name)

    # 지우는 과정
    answer = 0
    for file_name in remove_file_name_list:
        answer += trie.remove(file_name)

    if N_2 == 0:
        print(1)
    else:
        print(answer)