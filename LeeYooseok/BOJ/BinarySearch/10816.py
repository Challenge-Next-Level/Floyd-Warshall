from collections import Counter

n = int(input())
cards = list(map(int, input().split()))

new_cards_set = Counter(cards)
new_cards = list(new_cards_set.keys())
new_cards.sort()

m = int(input())
targets = list(map(int, input().split()))

result = list()
for t in targets:
    chk = False
    left, right = 0, len(new_cards)-1

    while left <= right:
        mid = (left + right) // 2

        if new_cards[mid] == t:
            chk = True
            print(new_cards_set[t], end=" ")
            break
        elif new_cards[mid] < t:
            left = mid + 1
        else:
            right = mid - 1

    if not chk:
        print(0, end=" ")
