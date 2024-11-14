import sys

input = sys.stdin.readline

from collections import defaultdict

N = (int(input()))

extension_dict = defaultdict(int)

for _ in range(N):
    S = input().rstrip()
    name, extension = S.split(".")

    extension_dict[extension] += 1

for extension in sorted(extension_dict, key=lambda x: x):
    print(extension, extension_dict[extension])