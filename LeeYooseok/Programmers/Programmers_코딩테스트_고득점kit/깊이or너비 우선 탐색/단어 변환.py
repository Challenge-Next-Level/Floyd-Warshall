from collections import defaultdict, deque


def solution(begin, target, words):
    if not target in words:
        return 0

    target_idx = 0

    graph = defaultdict(list)
    for idx in range(len(words)):
        word = words[idx]
        if sum(1 for a, b in zip(begin, word) if a != b) == 1:
            graph[begin].append([word, idx])

    for i in range(len(words)):
        word_1 = words[i]
        if word_1 == target:
            target_idx = i

        for j in range(i + 1, len(words)):
            word_2 = words[j]
            if sum(1 for a, b in zip(word_1, word_2) if a != b) == 1:
                graph[word_1].append([word_2, j])
                graph[word_2].append([word_1, i])

    visited = [-1 for _ in range(len(words))]

    queue = deque()
    queue.append([begin, 0])

    while queue:
        now_word, now_cnt = queue.popleft()

        for next_word, next_word_idx in graph[now_word]:
            if visited[next_word_idx] == -1:
                visited[next_word_idx] = now_cnt + 1
                queue.append([next_word, now_cnt + 1])
            elif visited[next_word_idx] > now_cnt + 1:
                visited[next_word_idx] = now_cnt + 1
                queue.append([next_word, now_cnt + 1])

    return visited[target_idx]