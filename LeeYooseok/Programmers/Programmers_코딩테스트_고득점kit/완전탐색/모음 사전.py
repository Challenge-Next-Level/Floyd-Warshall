from collections import deque

queue = deque()
def solution(word):
    alphabets = ['A', 'E', 'I', 'O', 'U']
    answer = 0

    for alphabet in alphabets:
        queue.append(alphabet)
        answer += 1

        while queue:
            new_string = queue.popleft()
            if new_string == word:
                return answer

            if len(new_string) == 5:
                continue

            for new_alphabet in alphabets:
                queue.append(new_string + new_alphabet)
                answer += 1
